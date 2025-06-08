# Sound Settings Implementation

## Overview
This implementation adds the ability to customize notification sound volume and type in the Open Super Whisper application.

## Features Added

### 1. Volume Control
- Users can adjust notification sound volume from 0% to 100%
- Volume setting is persistent across application restarts
- Real-time volume adjustment with visual feedback

### 2. Sound Type Selection
- Framework for different sound types/themes
- Currently includes "default" sound type with existing sounds
- Extensible design for adding more sound types in the future

### 3. Sound Settings Dialog
- New dedicated dialog for sound settings (`sound_settings_dialog.py`)
- Volume slider with percentage display
- Sound type dropdown selection
- Test playback button to preview sounds
- Save/Cancel functionality

### 4. Integration
- New toolbar button "通知音設定" (Sound Settings) 
- Settings are saved in QSettings for persistence
- All existing sound playback methods updated to use new volume and type settings

## Files Modified

### Configuration (`src/gui/resources/config.py`)
- Added `DEFAULT_SOUND_VOLUME = 0.5`
- Added `DEFAULT_SOUND_TYPE = "default"`
- Added `SOUND_TYPES` dictionary for extensible sound type management

### Labels (`src/gui/resources/labels.py`)
- Added `SOUND_SETTINGS = "通知音設定"`
- Added sound dialog labels: `SOUND_DIALOG_TITLE`, `SOUND_VOLUME_LABEL`, etc.

### Main Window (`src/gui/windows/main_window.py`)
- Added sound volume and type settings initialization
- Added `show_sound_settings_dialog()` method
- Added sound settings toolbar action
- Updated all sound playback methods to use configurable volume and sound type

## Files Created

### Sound Settings Dialog (`src/gui/components/dialogs/sound_settings_dialog.py`)
- Complete dialog implementation with volume slider and sound type selection
- Test sound functionality
- Proper integration with application settings

### Dialog Module (`src/gui/components/dialogs/__init__.py`)
- Added import for `SoundSettingsDialog`

## Usage

1. **Access Settings**: Click "通知音設定" in the toolbar
2. **Adjust Volume**: Use the horizontal slider (0-100%)
3. **Change Sound Type**: Select from dropdown (currently only "default" available)
4. **Test Sound**: Click "テスト再生" to preview the complete sound
5. **Save**: Click "保存" to apply changes

## Technical Details

### Volume Implementation
- Volume stored as float (0.0-1.0) in QSettings
- Slider displays percentage (0-100%) for user-friendly interface
- Applied to all three sound players (start, stop, complete)

### Sound Type Implementation
- Sound types defined in `AppConfig.SOUND_TYPES` dictionary
- Each type specifies paths for start, stop, and complete sounds
- Fallback to default paths if sound type not found

### Extensibility
To add new sound types:
1. Add sound files to assets directory
2. Add new entry to `AppConfig.SOUND_TYPES` dictionary
3. Sound type will automatically appear in the dropdown

## Testing
All sound playback methods have been updated to:
- Check if sound is enabled (`self.enable_sound`)
- Use configured volume (`self.sound_volume`)
- Use configured sound type (`self.sound_type`)
- Fallback gracefully if sound type is invalid