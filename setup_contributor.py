#!/usr/bin/env python3
"""
REE Contributor Setup Script
-----------------------------
EXPERIMENTAL — not fully tested on all configurations.
If you hit problems, follow the manual steps at:
  https://latent-fields.github.io/REE_assembly/docs/contribute.html

What this script does:
  1.  Checks Python version (must be 3.10–3.12)
  2.  Checks Git is installed
  3.  Asks where to clone the repos
  4.  Clones ree-v3 and REE_assembly (if not already present)
  5.  Installs torch + numpy with CUDA support (Windows/Linux) or plain (macOS)
  6.  Configures git commit identity (name + email)
  7.  Verifies CUDA / GPU
  8.  Collects machine details and writes a machine registration JSON
  9.  Commits and pushes the registration to REE_assembly
  10. Prints the command to start the experiment runner

Run with Python 3.12 specifically:
  Windows:  py -3.12 setup_contributor.py
  macOS:    python3.12 setup_contributor.py  (or python3 if 3.10–3.12)
  Linux:    python3.12 setup_contributor.py
"""

import sys
import subprocess
import os
import json
import platform
import shutil
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

IS_WIN = platform.system() == "Windows"

# Enable ANSI colours on Windows terminal
if IS_WIN:
    os.system("")


def ok(msg):   print(f"{GREEN}  ✓ {msg}{RESET}")
def warn(msg): print(f"{YELLOW}  ⚠ {msg}{RESET}")
def err(msg):  print(f"{RED}  ✗ {msg}{RESET}")
def info(msg): print(f"{CYAN}  → {msg}{RESET}")
def section(title): print(f"\n{BOLD}{'─'*60}\n  {title}\n{'─'*60}{RESET}")


def ask(prompt, default=None):
    suffix = f" [{default}]" if default else ""
    while True:
        val = input(f"  {prompt}{suffix}: ").strip()
        if val:
            return val
        if default is not None:
            return default
        print("  (required — please enter a value)")


def run(cmd, cwd=None, capture=False):
    """Run a command, return (returncode, stdout, stderr)."""
    result = subprocess.run(
        cmd, cwd=str(cwd) if cwd else None,
        capture_output=capture, text=True,
        encoding="utf-8", errors="replace",
    )
    return result.returncode, result.stdout, result.stderr


# ---------------------------------------------------------------------------
# Step 1 — Python version
# ---------------------------------------------------------------------------

section("Step 1 — Python version")
major, minor = sys.version_info[:2]
if (major, minor) < (3, 10) or (major, minor) > (3, 12):
    err(f"Python {major}.{minor} detected.")
    err("PyTorch CUDA builds require Python 3.10–3.12.")
    if IS_WIN:
        info("Install Python 3.12 from https://www.python.org (tick 'Add to PATH')")
        info("Then re-run: py -3.12 setup_contributor.py")
    sys.exit(1)
ok(f"Python {sys.version.split()[0]}")


# ---------------------------------------------------------------------------
# Step 2 — Git
# ---------------------------------------------------------------------------

section("Step 2 — Git")
git_path = shutil.which("git")
if not git_path:
    err("Git not found in PATH.")
    if IS_WIN:
        info("Install Git from https://git-scm.com/download/win")
    sys.exit(1)
rc, out, _ = run(["git", "--version"], capture=True)
ok(out.strip())


# ---------------------------------------------------------------------------
# Step 3 — Clone repos
# ---------------------------------------------------------------------------

section("Step 3 — Clone repos")
print()
print("  Repos will be cloned as siblings:")
print("    <parent>/")
print("    ├── ree-v3/")
print("    └── REE_assembly/")
print()

default_parent = str(Path.home() / "REE_Working")
parent_str = ask("Parent folder to clone into", default=default_parent)
parent = Path(parent_str).expanduser().resolve()

if not parent.exists():
    info(f"Creating {parent}")
    parent.mkdir(parents=True)

ORG = "Latent-Fields"
REPOS = ["ree-v3", "REE_assembly"]

for repo in REPOS:
    dest = parent / repo
    if dest.is_dir():
        ok(f"{repo} already present at {dest}")
    else:
        info(f"Cloning {repo}…")
        rc, _, stderr = run(
            ["git", "clone", f"https://github.com/{ORG}/{repo}.git"],
            cwd=parent, capture=True,
        )
        if rc != 0:
            err(f"Clone failed for {repo}:")
            print(f"    {stderr.strip()}")
            print()
            warn("Make sure you have been added to the Latent-Fields GitHub organisation.")
            warn("Request access at: https://github.com/orgs/Latent-Fields/teams")
            sys.exit(1)
        ok(f"Cloned {repo}")

ree_v3_dir    = parent / "ree-v3"
ree_asm_dir   = parent / "REE_assembly"


# ---------------------------------------------------------------------------
# Step 4 — Install PyTorch
# ---------------------------------------------------------------------------

section("Step 4 — Install PyTorch + numpy")

pip = [sys.executable, "-m", "pip"]

# Detect whether torch is already installed
rc, out, _ = run([sys.executable, "-c", "import torch; print(torch.__version__)"], capture=True)
if rc == 0:
    ok(f"torch {out.strip()} already installed")
else:
    if IS_WIN or platform.system() == "Linux":
        index_url = "https://download.pytorch.org/whl/cu124"
        info(f"Installing torch with CUDA support (index: {index_url})")
        # WSL2 note: CUDA works via the Windows NVIDIA driver — do NOT install
        # nvidia-driver via apt. The Windows driver handles GPU passthrough.
        if platform.system() == "Linux" and "microsoft" in platform.uname().release.lower():
            info("WSL2 detected — CUDA uses the Windows NVIDIA driver (already installed).")
            info("If torch.cuda.is_available() returns False, check: wsl --list --verbose")
            info("shows VERSION 2, and your Windows NVIDIA driver is up to date.")
        rc, _, stderr = run(
            pip + ["install", "torch", "numpy", "--index-url", index_url],
            capture=False,
        )
    else:
        info("macOS detected — installing CPU torch")
        rc, _, stderr = run(pip + ["install", "torch", "numpy"], capture=False)

    if rc != 0:
        err("pip install failed. Check the output above.")
        sys.exit(1)
    ok("torch + numpy installed")


# ---------------------------------------------------------------------------
# Step 5 — Git identity
# ---------------------------------------------------------------------------

section("Step 5 — Git commit identity")
print()
print("  Your name and email will appear in experiment commit messages.")
print("  This is separate from your GitHub login and must be set once per machine.")
print()

rc_name, cur_name, _ = run(["git", "config", "--global", "user.name"],  capture=True)
rc_mail, cur_mail, _ = run(["git", "config", "--global", "user.email"], capture=True)

cur_name = cur_name.strip()
cur_mail = cur_mail.strip()

if cur_name:
    ok(f"git user.name already set: {cur_name}")
    name = cur_name
else:
    name = ask("Your full name (for git commits)")
    run(["git", "config", "--global", "user.name", name])
    ok(f"Set git user.name = {name}")

if cur_mail:
    ok(f"git user.email already set: {cur_mail}")
else:
    email = ask("Your email (for git commits, can be GitHub noreply)")
    run(["git", "config", "--global", "user.email", email])
    ok(f"Set git user.email = {email}")


# ---------------------------------------------------------------------------
# Step 6 — CUDA / GPU check
# ---------------------------------------------------------------------------

section("Step 6 — GPU / CUDA check")

rc, out, _ = run(
    [sys.executable, "-c",
     "import torch; print('cuda:', torch.cuda.is_available()); "
     "print('gpu:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'none')"],
    capture=True,
)
if rc == 0:
    for line in out.strip().splitlines():
        if "cuda: True" in line or "gpu:" in line:
            ok(line.strip())
        elif "cuda: False" in line:
            warn(line.strip())
            warn("CUDA not available — experiments will run on CPU (very slow).")
            warn("Update NVIDIA drivers from https://www.nvidia.com if you have a CUDA GPU.")
else:
    warn("Could not run CUDA check — torch may not have installed correctly.")


# ---------------------------------------------------------------------------
# Step 7 — Machine registration
# ---------------------------------------------------------------------------

section("Step 7 — Register your machine")
print()
print("  This creates a small JSON file so compute contributions are tracked correctly.")
print("  The machine name must match the --machine flag you use when starting the runner.")
print()

import socket
default_machine = socket.gethostname()

machine_name  = ask("Machine name (no spaces, e.g. Daniel-PC)", default=default_machine)
owner         = ask("Your name", default=name)
display_name  = ask("Display name (e.g. 'CyberPower PC (i5-8600K + RTX 2060 Super)')")
hardware      = ask("Hardware (CPU, GPU, RAM in one line)")

while True:
    try:
        tdp = int(ask("CPU watts under load (check spec sheet or HWiNFO)", default="65"))
        break
    except ValueError:
        warn("Enter a number.")

while True:
    try:
        gpu_w = int(ask("GPU watts under load (0 if no GPU or CPU-only)", default="0"))
        break
    except ValueError:
        warn("Enter a number.")

reg = {
    "machine_name": machine_name,
    "display_name": display_name,
    "owner": owner,
    "hardware": hardware,
    "tdp_watts": tdp,
    "gpu_watts": gpu_w,
}

machines_dir = ree_asm_dir / "contributors" / "machines"
machines_dir.mkdir(parents=True, exist_ok=True)
reg_path = machines_dir / f"{machine_name}.json"

reg_path.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")
ok(f"Wrote {reg_path}")


# ---------------------------------------------------------------------------
# Step 8 — Commit and push registration
# ---------------------------------------------------------------------------

section("Step 8 — Push machine registration")

run(["git", "add", str(reg_path)], cwd=ree_asm_dir)
rc_diff, _, _ = run(["git", "diff", "--cached", "--quiet"], cwd=ree_asm_dir, capture=True)

if rc_diff == 0:
    ok("Machine registration already committed (no changes)")
else:
    rc_commit, _, cerr = run(
        ["git", "commit", "-m", f"register machine: {machine_name}"],
        cwd=ree_asm_dir, capture=True,
    )
    if rc_commit != 0:
        err("Git commit failed:"); print(f"    {cerr.strip()}")
        warn("You can push manually later: cd REE_assembly && git push origin HEAD:master")
    else:
        ok("Committed machine registration")
        rc_push, _, perr = run(
            ["git", "push", "origin", "HEAD:master"],
            cwd=ree_asm_dir, capture=True,
        )
        if rc_push != 0:
            warn("Push failed — you may need to authenticate with GitHub.")
            warn("Run:  gh auth login  (or complete browser login when prompted by git push)")
            warn("Then: cd REE_assembly && git push origin HEAD:master")
        else:
            ok("Pushed to REE_assembly")


# ---------------------------------------------------------------------------
# Step 9 — Generate experiment monitor launcher
# ---------------------------------------------------------------------------

section("Step 9 — Experiment monitor launcher")

if IS_WIN:
    launcher_path = parent / "start_monitor.bat"
    launcher_content = (
        f'@echo off\n'
        f'echo Starting REE Experiment Monitor on http://localhost:8001 ...\n'
        f'start "" "http://localhost:8001/REE_assembly/contributor_status.html"\n'
        f'cd /d "{parent}"\n'
        f'py -3.12 -m http.server 8001\n'
        f'pause\n'
    )
else:
    launcher_path = parent / "start_monitor.command"
    launcher_content = (
        f'#!/bin/bash\n'
        f'cd "{parent}"\n'
        f'echo "Starting REE Experiment Monitor on http://localhost:8001 ..."\n'
        f'sleep 1 && open "http://localhost:8001/REE_assembly/contributor_status.html" &\n'
        f'python3 -m http.server 8001\n'
    )

launcher_path.write_text(launcher_content, encoding="utf-8")
if not IS_WIN:
    import stat
    launcher_path.chmod(launcher_path.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

ok(f"Created launcher: {launcher_path}")
if IS_WIN:
    info("Double-click start_monitor.bat to open the experiment monitor in your browser.")
else:
    info("Double-click start_monitor.command to open the experiment monitor in your browser.")


# ---------------------------------------------------------------------------
# Done — print runner command
# ---------------------------------------------------------------------------

section("Setup complete!")
print()
print(f"  Start the experiment runner with:")
print()

runner_cmd = (
    f"  py -3.12 experiment_runner.py --auto-sync --loop --machine {machine_name}"
    if IS_WIN else
    f"  python3 experiment_runner.py --auto-sync --loop --machine {machine_name}"
)
print(f"{BOLD}{CYAN}{runner_cmd}{RESET}")
print()
print(f"  From inside: {ree_v3_dir}")
print()
info("Leave the runner terminal open. It will pick up queued experiments automatically.")
info("Results sync to REE_assembly and appear in the project explorer.")
info(f"Monitor experiments: double-click {launcher_path.name} in {parent}")
print()
print(f"{YELLOW}  Note: setup_contributor.py is experimental. If anything went wrong above,")
print(f"  follow the manual steps at:")
print(f"  https://latent-fields.github.io/REE_assembly/docs/contribute.html{RESET}")
print()
