#!/usr/bin/env python3
"""lit_distill.py -- paper-text-only Gemini pre-parse for the lit-pull workflow.

Takes ONE research paper (local PDF/text path or URL) and returns a compact,
structured JSON digest on stdout: design, sample, key results with verbatim
statistics, stated limitations, and exact quotes. The lit-pull skill reasons
over this digest instead of pulling a 30-page PDF into context; the REE claim
mapping, evidence_direction, and confidence calibration stay with the caller.

PRIVACY GUARANTEE (paper-text-only): the only thing sent to Gemini is the
published paper itself plus a fixed, domain-neutral extraction instruction.
No REE claim text, claims.yaml content, or any project context is ever
included in the request. Published papers are non-sensitive; this keeps the
free-tier "may be used to improve models" caveat off REE intellectual property.

Setup:
    pip install google-genai          # into /opt/local/bin/python3
    export GEMINI_API_KEY="AIza..."   # Google AI Studio key; aistudio.google.com/apikey

Usage:
    lit_distill.py <pdf-path-or-url> [--model M] [--out FILE]

stdout is strict JSON (ASCII-safe). All diagnostics go to stderr.
Exit codes: 0 ok | 2 usage/key error | 3 fetch error | 4 API error.
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.request

INLINE_LIMIT = 18 * 1024 * 1024  # Gemini inline-request practical ceiling
DEFAULT_MODEL = "gemini-2.5-flash"  # free-tier, 1M context, native PDF; override with --model

EXTRACTION_INSTRUCTION = (
    "You are extracting a faithful factual digest of a SINGLE research paper. "
    "Report only what the paper itself states; do not interpret, evaluate, or "
    "speculate beyond its contents. Copy all numbers, statistics, and effect "
    "sizes exactly as printed. Output STRICT JSON only, matching this shape:\n"
    "{\n"
    '  "source_title": str|null,\n'
    '  "authors": [str],\n'
    '  "year": int|null,\n'
    '  "venue": str|null,\n'
    '  "doi_or_url": str|null,\n'
    '  "study_type": "empirical|review|meta_analysis|theoretical|computational|other",\n'
    '  "design": str,                       // 1-3 sentences: what was done\n'
    '  "sample": {"n": str|null, "units": str|null, "species": str|null,\n'
    '             "population": str|null, "modality": str|null},\n'
    '  "methods_brief": str,\n'
    '  "key_results": [{"finding": str, "statistics_verbatim": str|null}],\n'
    '  "stated_limitations": [str],         // only limitations the paper itself states\n'
    '  "verbatim_quotes": [{"quote": str, "location_hint": str|null}],  // 4-8 short exact quotes\n'
    '  "extraction_caveats": str|null       // anything unreadable: scanned figures, truncation, etc.\n'
    "}\n"
    "verbatim_quotes must be copied character-for-character from the paper and be "
    "the sentences most useful for later checking whether a downstream claim is "
    "supported or contradicted. Return nothing except the JSON object."
)


def eprint(*a):
    print(*a, file=sys.stderr)


def looks_like_url(s):
    return s.startswith("http://") or s.startswith("https://")


def fetch_url(url, max_bytes, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "lit-distill/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        ctype = (r.headers.get("Content-Type") or "").lower()
        data = r.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("source exceeds --max-bytes (%d); pass a smaller or text source" % max_bytes)
    return data, ctype


def is_pdf(data, ctype, name):
    if data[:5] == b"%PDF-":
        return True
    if "application/pdf" in ctype:
        return True
    return name.lower().endswith(".pdf")


def build_part(data, pdf, types):
    if pdf:
        if len(data) > INLINE_LIMIT:
            raise ValueError(
                "PDF is %.1f MB, over the %d MB inline limit; pass a smaller PDF "
                "or a plain-text/HTML source instead" % (len(data) / 1e6, INLINE_LIMIT // (1024 * 1024))
            )
        return types.Part.from_bytes(data=data, mime_type="application/pdf")
    return types.Part(text=data.decode("utf-8", errors="replace"))


def main():
    ap = argparse.ArgumentParser(
        description="Paper-text-only Gemini digest for lit-pull. Sends ONLY the paper -- "
        "never REE claim context. JSON to stdout."
    )
    ap.add_argument("source", help="local PDF/text path OR http(s) URL of one paper")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Gemini model (default: %s)" % DEFAULT_MODEL)
    ap.add_argument("--out", help="write JSON to this file instead of stdout")
    ap.add_argument("--max-bytes", type=int, default=30 * 1024 * 1024, help="URL download cap (default 30MB)")
    ap.add_argument("--timeout", type=int, default=60, help="URL fetch timeout seconds (default 60)")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        eprint("ERROR: set GEMINI_API_KEY (Google AI Studio: aistudio.google.com/apikey).")
        return 2

    # Load the source bytes.
    try:
        if looks_like_url(args.source):
            data, ctype = fetch_url(args.source, args.max_bytes, args.timeout)
            src_kind = "url"
        else:
            if not os.path.isfile(args.source):
                eprint("ERROR: no such file: %s" % args.source)
                return 3
            with open(args.source, "rb") as f:
                data = f.read()
            ctype = ""
            src_kind = "file"
    except Exception as e:
        eprint("ERROR fetching source: %s" % e)
        return 3
    if not data:
        eprint("ERROR: source is empty.")
        return 3

    try:
        from google import genai
        from google.genai import types
    except Exception as e:
        eprint("ERROR: google-genai not installed (pip install google-genai): %s" % e)
        return 2

    try:
        pdf = is_pdf(data, ctype, args.source)
        part = build_part(data, pdf, types)
    except Exception as e:
        eprint("ERROR preparing source: %s" % e)
        return 3

    client = genai.Client(api_key=api_key)
    cfg = types.GenerateContentConfig(
        temperature=0,
        response_mime_type="application/json",
        system_instruction=EXTRACTION_INSTRUCTION,
    )
    try:
        resp = client.models.generate_content(
            model=args.model,
            contents=[part, "Extract the digest now."],
            config=cfg,
        )
        text = resp.text or ""
    except Exception as e:
        eprint("ERROR from Gemini API: %s" % e)
        return 4

    envelope = {
        "tool": "lit_distill",
        "schema": "lit_distill/v1",
        "model": args.model,
        "source": args.source,
        "source_kind": src_kind,
        "source_is_pdf": pdf,
        "source_bytes": len(data),
        "source_sha256": hashlib.sha256(data).hexdigest(),
    }
    try:
        envelope["extract"] = json.loads(text)
    except Exception:
        envelope["extract"] = None
        envelope["raw_text"] = text
        envelope["parse_error"] = "model did not return valid JSON; see raw_text"

    out = json.dumps(envelope, ensure_ascii=True, indent=2)
    if args.out:
        with open(args.out, "w") as f:
            f.write(out + "\n")
        eprint("wrote %s" % args.out)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
