@echo off
cd /d "%~dp0"
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
