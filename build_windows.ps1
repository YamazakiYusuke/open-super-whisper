# Windows PowerShell Build Script for Open Super Whisper
# Run this script on a Windows system to create a Windows executable

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Open Super Whisper - Windows Build" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.11+ from python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (!(Test-Path "venv_windows")) {
    Write-Host "Creating Windows virtual environment..." -ForegroundColor Yellow
    python -m venv venv_windows
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv_windows\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install pynput>=1.7.6 "numpy>=1.24.0,<2.0.0" openai>=1.0.0 pyinstaller>=6.13.0 pyqt6>=6.5.0 sounddevice>=0.4.6 soundfile>=0.12.1

# Check if assets directory exists
if (!(Test-Path "assets")) {
    Write-Host "ERROR: Assets directory not found" -ForegroundColor Red
    Write-Host "Please ensure you are running this script from the project root directory" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create the Windows executable
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Building Windows executable..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

python -m PyInstaller --onefile --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py

# Check if build was successful
if (Test-Path "dist\OpenSuperWhisper.exe") {
    $fileSize = (Get-Item "dist\OpenSuperWhisper.exe").Length
    $fileSizeMB = [math]::Round($fileSize / 1MB, 1)
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "BUILD SUCCESSFUL!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Executable created: dist\OpenSuperWhisper.exe" -ForegroundColor Green
    Write-Host "File size: $fileSizeMB MB ($fileSize bytes)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "The executable includes:" -ForegroundColor Yellow
    Write-Host "  - All Python dependencies" -ForegroundColor White
    Write-Host "  - PyQt6 GUI framework" -ForegroundColor White
    Write-Host "  - OpenAI API integration" -ForegroundColor White
    Write-Host "  - Translation functionality" -ForegroundColor White
    Write-Host "  - Audio processing libraries" -ForegroundColor White
    Write-Host "  - Application assets (icons, sounds)" -ForegroundColor White
    Write-Host ""
    Write-Host "You can now distribute dist\OpenSuperWhisper.exe" -ForegroundColor Green
    Write-Host "No Python installation required on target systems." -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "BUILD FAILED!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Check the output above for error messages." -ForegroundColor Yellow
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "  - Missing dependencies" -ForegroundColor White
    Write-Host "  - Insufficient disk space" -ForegroundColor White
    Write-Host "  - Antivirus software interference" -ForegroundColor White
    Write-Host ""
}

# Deactivate virtual environment
deactivate

Write-Host ""
Read-Host "Press Enter to exit"