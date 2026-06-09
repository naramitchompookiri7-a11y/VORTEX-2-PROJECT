# VORTEX AI v3.0 — Windows 11 Edition
### Virtual Operations & Real-Time EXecution
*Inspired by [JARVIS-MLX](https://github.com/huwprosser) by @huwprosser*

---

## Quick Start

```bat
REM Step 1 — install everything
python setup.py

REM Step 2 — set your Claude API key (optional but recommended)
set ANTHROPIC_API_KEY=sk-ant-...

REM Step 3 — launch VORTEX
python main.py
```

---

## Project Structure

```
VORTEX/
│
├── main.py                   ← Launch this
├── setup.py                  ← Run once to install deps
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py           ← All settings (API key, thresholds, colours)
│
├── memory/
│   └── store.py              ← Permanent JSON memory (~/.vortex_memory.json)
│
├── core/
│   └── monitor.py            ← CPU / RAM / Disk / Network (psutil)
│
├── agent/
│   └── brain.py              ← Claude API + smart local fallback brain
│
├── actions/
│   └── executor.py           ← Windows 11 system commands
│
├── voice/
│   ├── listener.py           ← VAD + SpeechRecognition / Whisper STT
│   ├── clap.py               ← Audio spike / clap wake detector
│   └── tts.py                ← Windows SAPI text-to-speech (pyttsx3)
│
├── vision/
│   └── gesture.py            ← OpenCV + MediaPipe hand gesture control
│
├── stt/
│   └── VoiceActivityDetection.py   ← VAD (from JARVIS-MLX)
│
└── ui/
    └── window.py             ← Full JARVIS-style tkinter native window
```

---

## Features

| Feature | Details |
|---|---|
| Native Window | Frameless dark sci-fi popup, draggable, JARVIS-style |
| Holographic Core | Animated rotating rings, pulsing sphere, scan sweep |
| Waveform Viz | 72-bar animated visualizer — reacts when VORTEX thinks |
| System Monitor | Live CPU, RAM, Disk, Network, Temp (psutil) |
| Clap Detection | Double-clap or audio spike → wakes VORTEX window |
| Voice Commands | Continuous VAD → Google STT or offline Whisper |
| Wake Words | "vortex", "hey vortex", "yo vortex" |
| Hand Gestures | OpenCV + MediaPipe: hover, grab/drag, swipe |
| TTS Voice | Windows SAPI via pyttsx3 (male voice) |
| Claude AI | Full Sonnet via API key; smart local fallback |
| Persistent Memory | Owner name, facts, preferences — stored forever |
| Quick Commands | One-click sidebar buttons |

---

## Voice & Clap Control

| Trigger | Action |
|---|---|
| Clap / loud knock | Wake VORTEX window |
| "Hey Vortex" | Activate and await command |
| "Vortex, open Chrome" | Launch Chrome |
| "Vortex, shutdown" | Power off PC |
| "Vortex, search AI news" | Google search |
| "Vortex, my name is Alex" | Remember your name |

---

## Hand Gesture Control

Activate via **Vision Core** button or say "activate vision".

| Gesture | Action |
|---|---|
| ✋ Open hand | Move desktop cursor (touchless hover) |
| ✊ Closed fist | Grab & drag active window (indicator turns orange) |
| 👋 Swipe left | Minimize active window |
| 👋 Swipe right | Restore/show window |
| ☝️ Index finger only | Left click |
| ✌️ Two fingers | Right click |

---

## System Commands

| Say / Type | What happens |
|---|---|
| shutdown / turn off | Shuts down PC in 5 seconds |
| restart / reboot | Restarts PC |
| sleep / hibernate | Suspends PC |
| open chrome / notepad / etc | Opens the app |
| search [query] | Google search in browser |
| screenshot | Saves to Desktop |
| volume 70 | Sets volume to 70% |
| my name is Alex | Permanently remembered |
| remember I use dark mode | Stored in memory forever |

---

## API Key Setup

```bat
REM Command Prompt
set ANTHROPIC_API_KEY=sk-ant-...

REM PowerShell
$env:ANTHROPIC_API_KEY='sk-ant-...'

REM Permanent (recommended) — add to .env in project folder:
ANTHROPIC_API_KEY=sk-ant-...
```

---

## Keyboard Shortcuts

| Key | Action |
|---|---|
| F4 | Toggle microphone mute |
| F11 | Toggle fullscreen |
| ESC | Minimize to taskbar |
| Enter | Send command |

---

## Requirements

- Python 3.10+ (from python.org — tick "tcl/tk and IDLE")
- Windows 10 or 11
- Microphone (for voice + clap detection)
- Webcam (optional — for hand gesture control)
- Internet (for Google STT + Claude API); fully offline mode available

---

## Credits

- JARVIS-MLX architecture by [@huwprosser](https://github.com/huwprosser)
- VAD: webrtcvad
- STT: SpeechRecognition (Google) / OpenAI Whisper
- TTS: pyttsx3 Windows SAPI
- Vision: OpenCV + MediaPipe
- AI: Anthropic Claude Sonnet
