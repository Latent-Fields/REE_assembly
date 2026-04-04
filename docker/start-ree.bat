@echo off
cd /d "%~dp0"

:: ── Step 1: SSH key setup ────────────────────────────────────────────────────
set KEY=%USERPROFILE%\.ssh\id_ed25519
set PUBKEY=%USERPROFILE%\.ssh\id_ed25519.pub

if not exist "%KEY%" (
    echo.
    echo No SSH key found. Generating one now...
    mkdir "%USERPROFILE%\.ssh" 2>nul
    ssh-keygen -t ed25519 -C "%COMPUTERNAME%" -f "%KEY%" -N ""
    echo.
    echo ============================================================
    echo  ACTION REQUIRED: Add your SSH key to GitHub
    echo ============================================================
    echo.
    echo  1. Copy the key shown below:
    echo.
    type "%PUBKEY%"
    echo.
    echo  2. Go to: https://github.com/settings/ssh/new
    echo     - Title: %COMPUTERNAME%
    echo     - Key type: Authentication Key
    echo     - Paste the key above
    echo     - Click "Add SSH key"
    echo.
    echo  Press any key here once you have added the key to GitHub.
    echo ============================================================
    pause >nul
) else (
    echo SSH key found: %KEY%
)

:: ── Step 2: Start container ──────────────────────────────────────────────────
echo.
echo Starting REE runner...
docker compose up -d
if %errorlevel% neq 0 (
    echo.
    echo Error: could not start Docker. Is Docker Desktop running?
    echo Install from: https://www.docker.com/products/docker-desktop/
    pause
    exit /b 1
)
echo.
echo Runner is starting. Opening Explorer in your browser...
timeout /t 5 /nobreak >nul
start http://localhost:8000/explorer
echo.
echo To stop:  docker compose down  (run from this folder)
pause
