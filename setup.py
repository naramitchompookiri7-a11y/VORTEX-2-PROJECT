"""
VORTEX AI v3.0 — Windows 11 Setup Script
=========================================
Run once before launching:
    python setup.py

This script:
  1. Checks Python version
  2. Checks tkinter (ships with Python on Windows)
  3. Installs all pip packages
  4. Checks for ANTHROPIC_API_KEY
  5. Prints a launch summary
"""

import subprocess
import sys
import os

BANNER = r"""
  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝
  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗
   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

         Virtual Operations & Real-Time EXecution
                  WINDOWS 11 SETUP v3.0
"""

# Packages installable via standard pip on Windows
PIP_PACKAGES = [
    ("anthropic",           "anthropic"),
    ("requests",            "requests"),
    ("pydantic",            "pydantic"),
    ("psutil",              "psutil"),
    ("SpeechRecognition",   "speech_recognition"),
    ("sounddevice",         "sounddevice"),
    ("numpy",               "numpy"),
    ("scipy",               "scipy"),
    ("pyttsx3",             "pyttsx3"),
    ("opencv-python",       "cv2"),
    ("mediapipe",           "mediapipe"),
    ("Pillow",              "PIL"),
    ("python-dotenv",       "dotenv"),
    ("webrtcvad-wheels",    "webrtcvad"),
]


def pip_install(package_name: str, quiet: bool = True) -> bool:
    args = [sys.executable, "-m", "pip", "install", package_name]
    if quiet:
        args.append("--quiet")
    result = subprocess.run(args, capture_output=True)
    return result.returncode == 0


def check_import(module: str) -> bool:
    try:
        __import__(module)
        return True
    except ImportError:
        return False


def main():
    print(BANNER)

    # ── Python version ────────────────────────────────────────────────────────
    v = sys.version_info
    if v < (3, 10):
        print(f"  ✗ Python 3.10+ required (you have {v.major}.{v.minor})")
        print("    Download from https://www.python.org/downloads/")
        sys.exit(1)
    print(f"  ✓ Python {v.major}.{v.minor}.{v.micro}")

    # ── tkinter ───────────────────────────────────────────────────────────────
    if check_import("tkinter"):
        import tkinter
        print(f"  ✓ tkinter {tkinter.TkVersion} (built-in)")
    else:
        print("  ✗ tkinter missing!")
        print("    Re-install Python from https://python.org and tick 'tcl/tk and IDLE'")

    # ── PyAudio special case ──────────────────────────────────────────────────
    print("\n  Installing packages (this may take a minute)...\n")
    if not check_import("pyaudio"):
        print("  → PyAudio: trying pipwin method...")
        pip_install("pipwin", quiet=True)
        result = subprocess.run(
            [sys.executable, "-m", "pipwin", "install", "pyaudio"],
            capture_output=True
        )
        if result.returncode != 0:
            # fallback: binary wheel
            pip_install("PyAudio", quiet=False)
        if check_import("pyaudio"):
            print("  ✓ pyaudio")
        else:
            print("  ⚠ pyaudio install failed — clap detection disabled")
            print("    Try manually: pip install PyAudio‑0.2.14‑cp311‑cp311‑win_amd64.whl")
            print("    from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio")
    else:
        print("  ✓ pyaudio (already installed)")

    # ── all other packages ────────────────────────────────────────────────────
    for pkg_name, import_name in PIP_PACKAGES:
        if check_import(import_name):
            print(f"  ✓ {pkg_name} (already installed)")
        else:
            print(f"  → Installing {pkg_name}...")
            ok = pip_install(pkg_name)
            status = "✓" if ok or check_import(import_name) else "⚠"
            print(f"  {status} {pkg_name}")

    # ── Whisper optional ──────────────────────────────────────────────────────
    print("\n  → Installing openai-whisper (offline STT, large download)...")
    pip_install("openai-whisper", quiet=True)
    print("  ✓ whisper")

    # ── API key check ─────────────────────────────────────────────────────────
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    print()
    if key:
        print(f"  ✓ ANTHROPIC_API_KEY found — Claude AI fully enabled!")
    else:
        print("  ⚠  ANTHROPIC_API_KEY not set — VORTEX will use local fallback brain.")
        print("     To enable Claude AI, run:")
        print("       set ANTHROPIC_API_KEY=sk-ant-...  (Command Prompt)")
        print("       $env:ANTHROPIC_API_KEY='sk-ant-...'  (PowerShell)")
        print("     Or add it to a .env file in the project folder.")

    # ── Done ──────────────────────────────────────────────────────────────────
    print("""
  ══════════════════════════════════════════
   Setup complete!  Launch VORTEX with:
       python main.py
  ══════════════════════════════════════════
""")


if __name__ == "__main__":
    main()
