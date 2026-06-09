"""
╔══════════════════════════════════════════════════════════╗
║            V O R T E X   A I   v3.0                     ║
║      Virtual Operations & Real-Time EXecution           ║
║                  Windows 11 Edition                      ║
║                                                          ║
║  Inspired by JARVIS-MLX by @huwprosser                  ║
╚══════════════════════════════════════════════════════════╝

Run:
    python main.py

Subsystems launched in parallel threads:
  ① Native tkinter desktop window  (JARVIS-style UI)
  ② Clap / audio-spike detector    (PyAudio)
  ③ Voice command listener         (SpeechRecognition / Whisper)
  ④ Hand-gesture vision core       (OpenCV + MediaPipe) — on demand
  ⑤ Real-time system monitor       (psutil)
  ⑥ Persistent memory              (JSON → ~/.vortex_memory.json)
  ⑦ AI brain                       (Claude API or local fallback)
  ⑧ TTS voice output               (pyttsx3 Windows SAPI)
"""

import sys
import os
import threading

# load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from config.settings  import Settings
from memory.store     import MemoryStore
from core.monitor     import SystemMonitor
from agent.brain      import VortexBrain
from actions.executor import ActionExecutor
from voice.listener   import VoiceListener
from voice.clap       import ClapDetector
from voice.tts        import VortexTTS
from ui.window        import VortexWindow


def print_banner():
    owner = ""
    try:
        mem = MemoryStore.__new__(MemoryStore)
        mem._lock = __import__("threading").Lock()
        mem._path = Settings.MEMORY_FILE
        mem._data = mem._load()
        owner = mem.get_owner() or "UNKNOWN"
    except Exception:
        owner = "UNKNOWN"

    api  = "✓ CLAUDE API ACTIVE" if Settings.ANTHROPIC_KEY else "✗ LOCAL FALLBACK MODE"
    print(f"""
  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝
  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗
   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

  AI  : {api}
  OWNER: {owner}
  MEM  : {Settings.MEMORY_FILE}
""")


def main():
    print_banner()

    # ── shared services ────────────────────────────────────────────────────────
    memory   = MemoryStore()
    monitor  = SystemMonitor()
    executor = ActionExecutor()
    tts      = VortexTTS()
    brain    = VortexBrain(memory, executor, tts)

    # ── UI (must live on main thread) ─────────────────────────────────────────
    window = VortexWindow(memory, monitor, brain, tts)

    # ── voice listener ────────────────────────────────────────────────────────
    voice = VoiceListener(
        on_command=lambda text: window.handle_voice_command(text),
        on_partial=lambda text: window.set_listening_text(text),
    )
    threading.Thread(target=voice.run, daemon=True, name="Voice").start()

    # ── clap detector ─────────────────────────────────────────────────────────
    clap = ClapDetector(on_clap=lambda: window.wake_up())
    threading.Thread(target=clap.run, daemon=True, name="Clap").start()

    print("  [VORTEX] All subsystems online. Window launching...\n")

    # ── blocking UI loop ──────────────────────────────────────────────────────
    window.run()


if __name__ == "__main__":
    main()
