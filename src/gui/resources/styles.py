"""
Clean Styles Module - Modern UI without gradients

This module provides a clean, modern design with clear status indicators
and no gradient backgrounds for optimal performance and clarity.
"""

class AppStyles:
    """Clean application styles manager"""

    # Modern Color Palette - Clean & Clear
    COLOR_PRIMARY = "#00D9FF"  # Cyan
    COLOR_RECORDING = "#FFD23F"  # Gold for recording
    COLOR_TRANSCRIBING = "#00D9FF"  # Cyan for transcribing
    COLOR_TRANSLATING = "#B47EDE"  # Purple for translating
    COLOR_SUCCESS = "#33FF88"  # Green for success

    # Main Window Style
    MAIN_WINDOW_STYLE = """
        * {
            font-family: "Segoe UI", Arial, sans-serif;
            font-size: 13px;
            color: #FFFFFF;
        }
        
        QMainWindow {
            background-color: rgba(20, 25, 40, 0.95);
            border: 2px solid rgba(0, 217, 255, 0.3);
            border-radius: 20px;
        }
        
        QToolBar {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            spacing: 8px;
            padding: 8px 15px;
            font-size: 13px;
            margin: 10px;
        }
        
        QPushButton {
            background-color: rgba(0, 217, 255, 0.2);
            color: white;
            border: 2px solid #00D9FF;
            border-radius: 15px;
            padding: 12px 20px;
            font-weight: bold;
            font-size: 14px;
        }
        
        QPushButton:hover {
            background-color: rgba(0, 217, 255, 0.4);
            border: 2px solid #00B8E6;
        }
        
        QTextEdit {
            background-color: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
            font-size: 14px;
            color: #FFFFFF;
            selection-background-color: rgba(0, 217, 255, 0.3);
        }
        
        QTextEdit:focus {
            border: 2px solid #00D9FF;
        }
        
        QComboBox {
            background-color: rgba(255, 255, 255, 0.08);
            border: 2px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 8px 15px;
            min-width: 150px;
            color: #FFFFFF;
        }
        
        QTabWidget {
            border: none;
            background-color: transparent;
        }
        
        QTabWidget::pane {
            border: 2px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            background-color: rgba(255, 255, 255, 0.03);
        }
        
        QTabBar::tab {
            background-color: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            border-bottom: none;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            padding: 8px 20px;
            margin-right: 2px;
            color: #FFFFFF;
            font-weight: bold;
        }
        
        QTabBar::tab:selected {
            background-color: rgba(0, 217, 255, 0.2);
            border: 2px solid #00D9FF;
            border-bottom: none;
            color: #00D9FF;
        }
        
        QTabBar::tab:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        QComboBox:hover {
            border: 2px solid #00D9FF;
            background-color: rgba(255, 255, 255, 0.12);
        }
        
        QLabel {
            color: #FFFFFF;
            font-size: 13px;
        }
    """

    # Control Panel Style
    CONTROL_PANEL_STYLE = """
        #controlPanel {
            background-color: rgba(255, 255, 255, 0.08);
            border: 2px solid rgba(255, 255, 255, 0.15);
            border-radius: 25px;
        }
    """

    # Record Button Styles
    RECORD_BUTTON_STYLE = """
        #recordButton {
            background-color: rgba(0, 217, 255, 0.2);
            color: white;
            border: 3px solid #00D9FF;
            border-radius: 25px;
            padding: 15px 30px;
            font-weight: bold;
            font-size: 16px;
        }
        
        #recordButton:hover {
            background-color: rgba(0, 217, 255, 0.4);
            border: 3px solid #00B8E6;
        }
    """

    RECORD_BUTTON_RECORDING_STYLE = """
        #recordButton {
            background-color: rgba(255, 210, 63, 0.3);
            color: white;
            border: 3px solid #FFD23F;
            border-radius: 25px;
            padding: 15px 30px;
            font-weight: bold;
            font-size: 16px;
        }
    """

    # Transcription Panel Style
    TRANSCRIPTION_PANEL_STYLE = """
        #transcriptionPanel {
            background-color: rgba(255, 255, 255, 0.06);
            border: 2px solid rgba(255, 255, 255, 0.12);
            border-radius: 25px;
        }
    """

    # Transcription Title Style
    TRANSCRIPTION_TITLE_STYLE = """
        color: #00D9FF;
        font-weight: bold;
        font-size: 18px;
        font-family: "Segoe UI", sans-serif;
        border: none;
        padding: 8px 0px;
        margin: 0px;
        background-color: transparent;
    """

    # Transcription Text Style
    TRANSCRIPTION_TEXT_STYLE = """
        border: none;
        background-color: rgba(255, 255, 255, 0.03);
        color: #FFFFFF;
        font-size: 15px;
        font-family: "Consolas", monospace;
        line-height: 1.6;
        padding: 15px;
        border-radius: 15px;
        selection-background-color: rgba(0, 217, 255, 0.3);
        min-height: 140px;
        max-height: 260px;
    """

    # Status Indicator Style
    STATUS_INDICATOR_STYLE = """
        #statusFrame {
            border-radius: 20px;
            background-color: rgba(30, 35, 50, 0.95);
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        #statusLabel {
            color: white;
            font-weight: bold;
            font-size: 15px;
            font-family: "Segoe UI", sans-serif;
            padding: 2px 5px;
            white-space: nowrap;
        }
        
        #timerLabel {
            color: #FFD23F;
            font-size: 22px;
            font-family: "Consolas", monospace;
            font-weight: 600;
            padding: 3px;
        }
        
        #statusIcon {
            font-size: 24px;
            padding: 4px;
            min-width: 30px;
        }
    """

    # Recording State (Gold)
    RECORDING_INDICATOR_FRAME_STYLE = """
        #statusFrame {
            border-radius: 20px;
            background-color: rgba(255, 210, 63, 0.2);
            border: 2px solid #FFD23F;
        }
    """
    
    # Transcribing State (Cyan)
    TRANSCRIBING_INDICATOR_FRAME_STYLE = """
        #statusFrame {
            border-radius: 20px;
            background-color: rgba(0, 217, 255, 0.2);
            border: 2px solid #00D9FF;
        }
    """
    
    # Translating State (Purple)
    TRANSLATING_INDICATOR_FRAME_STYLE = """
        #statusFrame {
            border-radius: 20px;
            background-color: rgba(180, 126, 222, 0.2);
            border: 2px solid #B47EDE;
        }
    """
    
    # Success/Completed State (Green)
    TRANSCRIBED_INDICATOR_FRAME_STYLE = """
        #statusFrame {
            border-radius: 20px;
            background-color: rgba(51, 255, 136, 0.2);
            border: 2px solid #33FF88;
        }
    """

    # Dialog Style
    API_KEY_DIALOG_STYLE = """
        QDialog {
            background-color: rgba(20, 25, 40, 0.95);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
        }
        
        QLineEdit {
            background-color: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 12px 15px;
            color: #FFFFFF;
            font-size: 14px;
        }
        
        QLineEdit:focus {
            border: 2px solid #00D9FF;
        }
        
        QPushButton {
            background-color: rgba(0, 217, 255, 0.2);
            color: white;
            border: 2px solid #00D9FF;
            border-radius: 15px;
            padding: 12px 20px;
            font-weight: bold;
            font-size: 14px;
        }
        
        QPushButton:hover {
            background-color: rgba(0, 217, 255, 0.4);
        }
        
        QLabel {
            color: #FFFFFF;
            font-size: 14px;
        }
    """

    # All other styles reference the base ones
    VOCABULARY_DIALOG_STYLE = API_KEY_DIALOG_STYLE
    SYSTEM_INSTRUCTIONS_DIALOG_STYLE = API_KEY_DIALOG_STYLE
    HOTKEY_DIALOG_STYLE = API_KEY_DIALOG_STYLE
    MAIN_WINDOW_STYLE_DARK = MAIN_WINDOW_STYLE
    TRANSCRIPTION_PANEL_STYLE_DARK = TRANSCRIPTION_PANEL_STYLE
    TRANSCRIPTION_TITLE_STYLE_DARK = TRANSCRIPTION_TITLE_STYLE
    TRANSCRIPTION_TEXT_STYLE_DARK = TRANSCRIPTION_TEXT_STYLE
    STATUS_BAR_STYLE = "color: rgba(255, 255, 255, 0.8); font-size: 13px;"
    RECORDING_INDICATOR_NORMAL_STYLE = "color: gray; font-size: 16px;"
    RECORDING_INDICATOR_ACTIVE_STYLE = "color: #FFD23F; font-size: 18px; font-weight: bold;"
    RECORDING_TIMER_LABEL_STYLE = "color: #FFD23F; font-family: monospace; font-weight: bold;"
    RECORDING_INDICATOR_INACTIVE_STYLE = "color: rgba(255, 255, 255, 0.5); font-size: 16px;"
    SYSTEM_TRAY_MENU_STYLE = API_KEY_DIALOG_STYLE
    API_KEY_INFO_LABEL_STYLE = "color: rgba(255, 255, 255, 0.8); padding: 5px 0;"