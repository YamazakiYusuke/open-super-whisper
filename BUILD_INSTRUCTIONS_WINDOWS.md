# Windows Executable Build Instructions

This guide will help you create a Windows executable (.exe) for Open Super Whisper on a Windows system.

## Prerequisites

1. **Windows 10/11** (recommended)
2. **Python 3.11+** installed from [python.org](https://www.python.org/downloads/)
3. **Git** (optional, for cloning the repository)

## Quick Build (Automated)

### Method 1: Using PowerShell (Recommended)

1. Open **PowerShell** as Administrator
2. Navigate to the project directory:
   ```powershell
   cd path\to\open-super-whisper
   ```
3. Run the build script:
   ```powershell
   .\build_windows.ps1
   ```

### Method 2: Using Command Prompt

1. Open **Command Prompt** as Administrator
2. Navigate to the project directory:
   ```cmd
   cd path\to\open-super-whisper
   ```
3. Run the build script:
   ```cmd
   build_windows.bat
   ```

## Manual Build Instructions

If the automated scripts don't work, follow these manual steps:

### Step 1: Create Virtual Environment

```cmd
python -m venv venv_windows
venv_windows\Scripts\activate.bat
```

### Step 2: Install Dependencies

```cmd
python -m pip install --upgrade pip
pip install pynput>=1.7.6 numpy>=1.24.0 openai>=1.0.0 pyinstaller>=6.13.0 pyqt6>=6.5.0 sounddevice>=0.4.6 soundfile>=0.12.1
```

### Step 3: Build Executable

```cmd
python -m PyInstaller --onefile --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py
```

## Expected Output

After successful build, you'll find:
- **Executable**: `dist\OpenSuperWhisper.exe`
- **Size**: Approximately 30-50 MB
- **Dependencies**: All included (no Python required on target systems)

## Build Features

The Windows executable includes:

✅ **Complete Translation System**
- OpenAI Chat API integration
- 20 language support
- 3-tier model selection (Economy/Standard/Premium)
- Tabbed UI (Original/Translation)

✅ **Audio Processing**
- PyQt6 GUI framework
- Sound recording and playback
- Multiple audio format support

✅ **Self-Contained**
- No Python installation required
- All dependencies bundled
- Assets (icons, sounds) included

## Distribution

The generated `OpenSuperWhisper.exe` can be:
- ✅ Copied to any Windows system
- ✅ Distributed via email, cloud storage, or USB
- ✅ Run directly without installation
- ✅ Used on systems without Python

## Troubleshooting

### Common Issues:

1. **Python not found**
   - Install Python from python.org
   - Ensure Python is added to PATH

2. **Permission denied**
   - Run PowerShell/Command Prompt as Administrator
   - Check antivirus software settings

3. **Build fails with missing modules**
   - Update pip: `python -m pip install --upgrade pip`
   - Install missing dependencies manually

4. **Antivirus interference**
   - Temporarily disable antivirus during build
   - Add project directory to antivirus exclusions

5. **Insufficient disk space**
   - Ensure at least 1GB free space
   - Build process creates temporary files

### Environment Variables

If you encounter import errors, you may need to set:
```cmd
set PYTHONPATH=%cd%
```

## Testing the Executable

1. Navigate to `dist` folder
2. Double-click `OpenSuperWhisper.exe`
3. The application should start with GUI
4. Test basic functionality:
   - GUI loads properly
   - Translation settings dialog opens
   - Audio permissions work

## Advanced Build Options

### Debug Build (with console)
```cmd
python -m PyInstaller --onefile --console --icon assets/icon.ico --name "OpenSuperWhisper_Debug" --add-data "assets;assets" main.py
```

### Directory Build (faster startup)
```cmd
python -m PyInstaller --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py
```

## Deployment Notes

- **System Requirements**: Windows 10+ (64-bit)
- **Audio Libraries**: Usually pre-installed on modern Windows
- **OpenAI API Key**: Required for transcription and translation
- **Internet Connection**: Required for API-based features
- **Local Models**: Require FFmpeg for local transcription mode

---

## Support

For build issues, check:
1. Python version compatibility
2. All dependencies installed correctly  
3. Assets directory present in project root
4. Sufficient permissions and disk space
5. Antivirus not blocking PyInstaller