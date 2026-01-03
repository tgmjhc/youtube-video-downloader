@echo off
echo ================================
echo VidExtract Quick Setup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python is not installed!
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python found

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X pip is not installed!
    pause
    exit /b 1
)

echo [OK] pip found

REM Install requirements
echo.
echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo [OK] Dependencies installed successfully
) else (
    echo X Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the server, run:
echo   python server.py
echo.
echo Then open index.html in your browser
echo.
pause
