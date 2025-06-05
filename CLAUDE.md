# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Open Super Whisper is a desktop application for speech-to-text transcription with global hotkey control. It's built with PyQt6 and supports both OpenAI API and local Whisper models.

## Essential Development Commands

### Running the Application
```bash
# Install dependencies
uv sync

# Run the application
python main.py

# Run minimized to system tray
python main.py -m
```

### Building Executables
```bash
# Windows
python -m PyInstaller --onefile --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py

# macOS
python -m PyInstaller --onefile --windowed --icon assets/icon.icns --name "OpenSuperWhisper" --add-data "assets:assets" main.py

# Linux
python -m PyInstaller --onefile --windowed --icon assets/linux_pngs/icon_256.png --name "OpenSuperWhisper" --add-data "assets:assets" main.py
```

### Testing
```bash
# Test local whisper functionality
python test_whisper.py

# Debug temporary recording files
python debug_temp_files.py
```

## Architecture Overview

### Core Module Structure (`src/core/`)
- **audio_recorder.py**: Audio recording using sounddevice, handles WAV file creation
- **hotkeys.py**: Global hotkey management with pynput, thread-safe implementation
- **transcription_manager.py**: Unified interface abstracting API vs local transcription
- **whisper_api.py**: OpenAI API integration with custom vocabulary and system instructions
- **whisper_local.py**: Local Whisper model management with auto-download and caching

### GUI Architecture (`src/gui/`)
- **main.py**: QApplication setup and system tray integration
- **windows/main_window.py**: Main window with toolbar, status indicator, and transcription area
- **components/dialogs/**: Modular dialogs for API key, hotkey, vocabulary, and model loading
- **resources/config.py**: Centralized configuration management with QSettings persistence

### Key Design Patterns
1. **Dual Mode Architecture**: Seamless switching between API and local transcription modes
2. **Thread Safety**: Audio recording and transcription run in separate QThreads
3. **Signal-Slot Communication**: PyQt6 signals for clean inter-component communication
4. **System Tray Integration**: Application persists in background with global hotkey support

### Important Implementation Details
- Audio is recorded as 16kHz mono WAV files for optimal Whisper compatibility
- Temporary audio files are stored in system temp directory and cleaned up after transcription
- Configuration persists across sessions using QSettings
- Local models are downloaded to `~/.cache/whisper/` on first use
- Dark theme detection uses Windows registry on Windows platform