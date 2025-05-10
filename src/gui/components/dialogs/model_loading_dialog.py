from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import Qt

class ModelLoadingDialog(QDialog):
    """Whisperローカルモデルのロード中に表示するダイアログ"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Loading Model")
        self.setFixedSize(300, 100)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)
        self.setModal(True)
        
        # レイアウト
        layout = QVBoxLayout()
        
        # ラベル
        self.label = QLabel("Loading Whisper model...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # プログレスバー (不定)
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)  # インディケーターモード
        layout.addWidget(self.progress)
        
        self.setLayout(layout) 