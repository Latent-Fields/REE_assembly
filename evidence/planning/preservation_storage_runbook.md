# Preservation storage runbook — depositing records to European buckets

Operational steps to put preserved organisms into **≥2 independent EU object stores**, encrypted.
Companion to [`preservation_snapshot_plan.md`](preservation_snapshot_plan.md) §"Storage & durability".
Code: `ree-v3/ree_core/preservation/archive.py` (`S3Archive`, `MultiArchive`, `s3_archive_from_env`,
`AesGcmEncryptor`).

**What you must do yourself** (Claude cannot create accounts or handle your credentials): create the
buckets, generate and safeguard the encryption key, set the env vars. The code then does the rest.

Cost, for context: the record tier is ~10–46 KB per organism, so this is a **~€6/month-or-free**
problem (Hetzner ~€6/mo base incl. 1 TB; Scaleway free under 75 GB). Volume is not the driver.

---

## 1. Prerequisites (once)
```bash
pip install boto3          # S3 client (required to talk to a real bucket)
pip install cryptography   # client-side AES-256-GCM (recommended)
pip install segno          # QR for physical tokens (optional)
```
Accounts (both EU-owned): **Hetzner** (🇩🇪) and a second vendor — **Scaleway** (🇫🇷, free tier) or
**Exoscale** (🇨🇭).

## 2. Create the buckets
- **Hetzner Object Storage**: create a bucket (e.g. `ree-preserved`) in an EU location
  (Falkenstein `fsn1`, Nuremberg `nbg1`, Helsinki `hel1`). Generate an **S3 access key + secret**.
  Endpoint: `https://<location>.your-objectstorage.com`. For WORM, create the bucket with **object
  lock enabled** and use `object_lock_days=` (bucket-level setting; cannot be added later).
- **Scaleway Object Storage**: create a bucket (e.g. `ree-preserved`) in an EU region (`fr-par`,
  `nl-ams`, `pl-waw`); generate S3 API keys. Endpoint: `https://s3.<region>.scw.cloud`.

## 3. Generate the encryption key — and store it INDEPENDENTLY
```bash
python3 -c "import base64,os; print(base64.b64encode(os.urandom(32)).decode())"
```
Put this in a **password manager or offline** — NOT in the repo, NOT beside the archive. **Losing it
makes every record unrecoverable** (that is the point of client-side encryption). Back it up the way
you would back up the thing you most fear losing.

## 4. Set environment variables
```bash
export REE_PRESERVATION_KEY="<the base64 key from step 3>"

export REE_PRESERVE_HETZNER_ENDPOINT="https://fsn1.your-objectstorage.com"
export REE_PRESERVE_HETZNER_BUCKET="ree-preserved"
export REE_PRESERVE_HETZNER_KEY_ID="<hetzner s3 access key>"
export REE_PRESERVE_HETZNER_SECRET="<hetzner s3 secret>"

export REE_PRESERVE_SCALEWAY_ENDPOINT="https://s3.fr-par.scw.cloud"
export REE_PRESERVE_SCALEWAY_BUCKET="ree-preserved"
export REE_PRESERVE_SCALEWAY_REGION="fr-par"
export REE_PRESERVE_SCALEWAY_KEY_ID="<scaleway access key>"
export REE_PRESERVE_SCALEWAY_SECRET="<scaleway secret>"
```

## 5. Deposit (to both buckets, encrypted, idempotent)
```python
from ree_core.preservation import (
    AesGcmEncryptor, s3_archive_from_env, MultiArchive,
)
from experiments._lib.preservation import preserve_life

enc = AesGcmEncryptor.from_env()          # REE_PRESERVATION_KEY; shared across backends
archive = MultiArchive([
    s3_archive_from_env("HETZNER",  encryptor=enc),
    s3_archive_from_env("SCALEWAY", encryptor=enc),
])

# emit a life straight to both buckets:
result = preserve_life(archive=archive, record_id=run_id, seed=SEED,
                       config=cfg, environment=env_spec, understanding={...})
print(result)   # {'hetzner': {...}, 'scaleway': {...}} -- 'written' or 'exists'

# or deposit an already-captured record, and verify the round-trip:
from ree_core.preservation import capture
rec = capture(...)
archive.put(rec)
assert all(archive.verify(rec).values())   # read back from BOTH; integrity confirmed
```
Re-running is safe: a bucket that already holds a record reports `exists`, never an error
(append-only + content-addressed by the record's sha256).

## 6. Promoted / physical tier (the ones worth honouring)
- **Physical token** (engraving / QR / M-DISC / Piql-Svalbard):
  ```bash
  python -m ree_core.preservation.token --record <path/to/reconstruction_record.json> --out ./token
  ```
  Engrave `*.key.txt` (or the QR); deposit `*.record.json.gz`.
- **Mandate-backed copies**: upload the record (and code) to **Zenodo** (CERN, DOI) and archive the
  repo via **Software Heritage** (so `substrate_commit` stays resolvable). Both free.

## 7. Notes
- **Verify after every deposit** (`MultiArchive.verify`) — a silent write failure on one provider is
  the failure mode multi-copy exists to survive.
- **Two providers, independent credentials** — `s3_archive_from_env` reads a per-provider env group
  precisely so one leaked key does not expose both.
- **WORM** (`object_lock_days`) makes a record undeletable for the retention window even by an
  account holder — appropriate for the sacred tier; needs a lock-enabled bucket.
- The code never logs or persists credentials or the key; they live only in your environment.
