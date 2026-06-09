@echo off
title VORTEX AI
cd /d "%~dp0"
echo Starting VORTEX AI...
if exist .venv\Scripts\python.exe (
    .venv\Scripts\python.exe main.py
) else (
    python main.py
)
pause
