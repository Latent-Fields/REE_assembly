"""
REE System Tray Icon
--------------------
Connects to a running REE serve.py and shows runner status in the system tray.

Usage:
    python3 ree_tray.py
    REE_TRAY_HOST=192.168.1.10:8000 python3 ree_tray.py  # remote host

Dependencies:
    pip install pystray Pillow requests

Build distributable binary:
    bash build_tray.sh
"""

import os
import sys
import threading
import time
import webbrowser
from typing import Optional

try:
    import pystray
    from PIL import Image, ImageDraw
    import requests
except ImportError as e:
    sys.exit(
        f"Missing dependency: {e}\n"
        "Install with: pip install pystray Pillow requests"
    )

# ── Config ────────────────────────────────────────────────────────────────────

HOST = os.environ.get("REE_TRAY_HOST", "localhost:8000")
BASE_URL = f"http://{HOST}"
POLL_INTERVAL = 5  # seconds between status checks

# ── Icon generation ───────────────────────────────────────────────────────────

_ICON_SIZE = 64
_CIRCLE_MARGIN = 8


def _make_icon(color: str) -> Image.Image:
    """Draw a solid circle on a transparent background."""
    img = Image.new("RGBA", (_ICON_SIZE, _ICON_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    m = _CIRCLE_MARGIN
    draw.ellipse(
        [m, m, _ICON_SIZE - m, _ICON_SIZE - m],
        fill=color,
    )
    return img


# Pre-render the three states
_ICON_GREEN  = _make_icon("#22c55e")   # runner running
_ICON_ORANGE = _make_icon("#f97316")   # serve up, runner stopped
_ICON_RED    = _make_icon("#ef4444")   # serve unreachable


# ── State ─────────────────────────────────────────────────────────────────────

class State:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.v3_running: bool = False
        self.v2_running: bool = False
        self.serve_up: bool = False
        self.current_experiment: str = ""
        self.queue_depth: int = 0
        self.error: str = ""

    def update_from_status(self, data: dict) -> None:
        with self.lock:
            self.serve_up = True
            self.error = ""
            self.v3_running = data.get("v3", {}).get("running", False)
            self.v2_running = data.get("v2", {}).get("running", False)

    def update_from_runner_status(self, data: dict) -> None:
        """Parse runner_status.json for current experiment info."""
        with self.lock:
            current = data.get("current")
            if current:
                qid = current.get("queue_id", "")
                script = current.get("script", "")
                # Show queue_id if available, else basename of script
                if qid:
                    self.current_experiment = qid
                elif script:
                    self.current_experiment = script.split("/")[-1]
                else:
                    self.current_experiment = ""
            else:
                self.current_experiment = ""
            remaining = data.get("queue_remaining", data.get("items_remaining", 0))
            self.queue_depth = remaining if isinstance(remaining, int) else 0

    def mark_serve_down(self, err: str) -> None:
        with self.lock:
            self.serve_up = False
            self.v3_running = False
            self.v2_running = False
            self.current_experiment = ""
            self.error = err

    def icon_image(self) -> Image.Image:
        with self.lock:
            if not self.serve_up:
                return _ICON_RED
            if self.v3_running or self.v2_running:
                return _ICON_GREEN
            return _ICON_ORANGE

    def tooltip(self) -> str:
        with self.lock:
            if not self.serve_up:
                return f"REE -- serve.py unreachable ({HOST})"
            parts = []
            if self.v3_running:
                parts.append("V3 running")
                if self.current_experiment:
                    parts.append(self.current_experiment)
                if self.queue_depth:
                    parts.append(f"{self.queue_depth} queued")
            elif self.v2_running:
                parts.append("V2 running")
            else:
                parts.append("Idle")
            return "REE -- " + " | ".join(parts) if parts else "REE"

    def runner_label(self) -> str:
        with self.lock:
            if not self.serve_up:
                return "serve.py unreachable"
            if self.v3_running:
                label = "V3 Runner: Running"
                if self.current_experiment:
                    label += f" ({self.current_experiment})"
                return label
            if self.v2_running:
                return "V2 Runner: Running"
            return "Runner: Stopped"

    def any_running(self) -> bool:
        with self.lock:
            return self.v3_running or self.v2_running


_state = State()

# ── API helpers ───────────────────────────────────────────────────────────────

_SESSION = requests.Session()
_SESSION.timeout = 4


def _get(path: str) -> Optional[dict]:
    try:
        r = _SESSION.get(f"{BASE_URL}{path}")
        r.raise_for_status()
        return r.json()
    except Exception:
        return None


def _post(path: str) -> Optional[dict]:
    try:
        r = _SESSION.post(f"{BASE_URL}{path}")
        r.raise_for_status()
        return r.json()
    except Exception:
        return None


# ── Poll thread ───────────────────────────────────────────────────────────────

def _poll(icon: pystray.Icon) -> None:
    while True:
        data = _get("/api/runner/status")
        if data is None:
            _state.mark_serve_down("connection refused")
        else:
            _state.update_from_status(data)
            # Also fetch richer runner_status for current experiment name
            rs = _get("/evidence/experiments/runner_status.json")
            if rs:
                _state.update_from_runner_status(rs)

        icon.icon = _state.icon_image()
        icon.title = _state.tooltip()
        _rebuild_menu(icon)
        time.sleep(POLL_INTERVAL)


# ── Menu ──────────────────────────────────────────────────────────────────────

def _open_explorer(_icon, _item) -> None:
    webbrowser.open(f"{BASE_URL}/explorer")


def _start_v3(_icon, _item) -> None:
    result = _post("/api/runner/v3/start")
    if result is None:
        print("[ree_tray] start failed -- serve.py unreachable", flush=True)


def _stop_runner(_icon, _item) -> None:
    result = _post("/api/runner/stop")
    if result is None:
        print("[ree_tray] stop failed -- serve.py unreachable", flush=True)


def _quit(icon: pystray.Icon, _item) -> None:
    icon.stop()


def _build_menu() -> pystray.Menu:
    running = _state.any_running()
    serve_up = _state.serve_up

    items = [
        pystray.MenuItem("Open Explorer", _open_explorer, default=True),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(_state.runner_label(), None, enabled=False),
    ]

    if serve_up:
        if running:
            items.append(pystray.MenuItem("Stop Runner", _stop_runner))
        else:
            items.append(pystray.MenuItem("Start V3 Runner", _start_v3))

    items += [
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Quit", _quit),
    ]

    return pystray.Menu(*items)


def _rebuild_menu(icon: pystray.Icon) -> None:
    icon.menu = _build_menu()


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    print(f"[ree_tray] Connecting to {BASE_URL}", flush=True)

    icon = pystray.Icon(
        name="ree",
        icon=_ICON_RED,
        title="REE -- starting...",
        menu=_build_menu(),
    )

    # Start polling in background thread
    t = threading.Thread(target=_poll, args=(icon,), daemon=True)
    t.start()

    icon.run()


if __name__ == "__main__":
    main()
