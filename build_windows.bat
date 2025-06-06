@echo off
REM Windows Build Script for Open Super Whisper
REM Run this script on a Windows system to create a Windows executable

echo ========================================
echo Open Super Whisper - Windows Build
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from python.org
    pause
    exit /b 1
)

echo Python found. Checking version...
python -c "import sys; print(f'Python {sys.version}')"
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv_windows" (
    echo Creating Windows virtual environment...
    python -m venv venv_windows
)

REM Activate virtual environment
echo Activating virtual environment...
call venv_windows\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install pynput>=1.7.6 numpy>=1.24.0 openai>=1.0.0 pyinstaller>=6.13.0 pyqt6>=6.5.0 sounddevice>=0.4.6 soundfile>=0.12.1

REM Check if assets directory exists
if not exist "assets" (
    echo ERROR: Assets directory not found
    echo Please ensure you are running this script from the project root directory
    pause
    exit /b 1
)

REM Create the Windows executable
echo.
echo ========================================
echo Building Windows executable...
echo ========================================
python -m PyInstaller --onefile --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py

REM Check if build was successful
if exist "dist\OpenSuperWhisper.exe" (
    echo.
    echo ========================================
    echo BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Executable created: dist\OpenSuperWhisper.exe
    dir /B dist\OpenSuperWhisper.exe
    echo.
    echo File size:
    for %%I in (dist\OpenSuperWhisper.exe) do echo   %%~zI bytes (%%~zI bytes)
    echo.
    echo The executable includes:
    echo   - All Python dependencies
    echo   - PyQt6 GUI framework
    echo   - OpenAI API integration
    echo   - Translation functionality
    echo   - Audio processing libraries
    echo   - Application assets (icons, sounds)
    echo.
    echo You can now distribute dist\OpenSuperWhisper.exe
    echo No Python installation required on target systems.
    echo.
) else (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    echo.
    echo Check the output above for error messages.
    echo Common issues:
    echo   - Missing dependencies
    echo   - Insufficient disk space
    echo   - Antivirus software interference
    echo.
)

REM Deactivate virtual environment
deactivate

echo.
echo Press any key to exit...
pause >nul