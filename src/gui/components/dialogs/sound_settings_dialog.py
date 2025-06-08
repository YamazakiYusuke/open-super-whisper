"""
サウンド設定用のダイアログモジュール

通知音の音量とタイプを設定するためのダイアログを提供します
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLabel, QSlider, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

from src.gui.resources.labels import AppLabels
from src.gui.resources.styles import AppStyles
from src.gui.resources.config import AppConfig
from src.gui.utils.resource_helper import getResourcePath

class SoundSettingsDialog(QDialog):
    """
    サウンド設定を管理するダイアログ
    
    通知音の音量とタイプを設定するためのダイアログウィンドウ
    """
    
    def __init__(self, parent=None, current_volume=0.5, current_sound_type="default"):
        """
        SoundSettingsDialogの初期化
        
        Parameters
        ----------
        parent : QWidget, optional
            親ウィジェット
        current_volume : float, optional
            現在の音量設定（0.0-1.0）
        current_sound_type : str, optional
            現在のサウンドタイプ
        """
        super().__init__(parent)
        self.setWindowTitle(AppLabels.SOUND_DIALOG_TITLE)
        self.setMinimumWidth(400)
        
        # テスト再生用のプレーヤー
        self.test_player = QMediaPlayer()
        self.test_audio_output = QAudioOutput()
        self.test_player.setAudioOutput(self.test_audio_output)
        
        # スタイルシートを設定
        self.setStyleSheet(AppStyles.API_KEY_DIALOG_STYLE)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # フォームレイアウト
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        
        # 音量スライダー
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(int(current_volume * 100))
        self.volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(25)
        
        # 音量表示ラベル
        self.volume_label = QLabel(f"{int(current_volume * 100)}%")
        self.volume_label.setMinimumWidth(40)
        self.volume_slider.valueChanged.connect(self.update_volume_label)
        
        # 音量のレイアウト
        volume_layout = QHBoxLayout()
        volume_layout.addWidget(self.volume_slider)
        volume_layout.addWidget(self.volume_label)
        
        form_layout.addRow(AppLabels.SOUND_VOLUME_LABEL, volume_layout)
        
        # サウンドタイプコンボボックス
        self.sound_type_combo = QComboBox()
        for sound_id, sound_config in AppConfig.SOUND_TYPES.items():
            self.sound_type_combo.addItem(sound_config["name"], sound_id)
        
        # 現在のサウンドタイプを選択
        current_index = self.sound_type_combo.findData(current_sound_type)
        if current_index >= 0:
            self.sound_type_combo.setCurrentIndex(current_index)
        
        form_layout.addRow(AppLabels.SOUND_TYPE_LABEL, self.sound_type_combo)
        
        layout.addLayout(form_layout)
        
        # 情報テキスト
        volume_info_label = QLabel(AppLabels.SOUND_VOLUME_INFO)
        volume_info_label.setWordWrap(True)
        volume_info_label.setStyleSheet(AppStyles.API_KEY_INFO_LABEL_STYLE)
        layout.addWidget(volume_info_label)
        
        type_info_label = QLabel(AppLabels.SOUND_TYPE_INFO)
        type_info_label.setWordWrap(True)
        type_info_label.setStyleSheet(AppStyles.API_KEY_INFO_LABEL_STYLE)
        layout.addWidget(type_info_label)
        
        # テストボタン
        test_layout = QHBoxLayout()
        self.test_button = QPushButton(AppLabels.SOUND_TEST_BUTTON)
        self.test_button.clicked.connect(self.test_sound)
        test_layout.addWidget(self.test_button)
        test_layout.addStretch()
        layout.addLayout(test_layout)
        
        # 保存・キャンセルボタン
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        self.save_button = QPushButton(AppLabels.SAVE_BUTTON)
        self.save_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton(AppLabels.CANCEL_BUTTON)
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def update_volume_label(self, value):
        """音量ラベルを更新する"""
        self.volume_label.setText(f"{value}%")
    
    def test_sound(self):
        """選択されているサウンドをテスト再生する"""
        current_sound_type = self.sound_type_combo.currentData()
        if current_sound_type and current_sound_type in AppConfig.SOUND_TYPES:
            # 完了音をテストとして再生
            sound_path = getResourcePath(AppConfig.SOUND_TYPES[current_sound_type]["complete"])
            self.test_player.setSource(QUrl.fromLocalFile(sound_path))
            
            # 現在の音量設定を適用
            volume = self.volume_slider.value() / 100.0
            self.test_audio_output.setVolume(volume)
            
            self.test_player.play()
    
    def get_volume(self):
        """
        現在の音量設定を返す
        
        Returns
        -------
        float
            音量（0.0-1.0）
        """
        return self.volume_slider.value() / 100.0
    
    def get_sound_type(self):
        """
        現在のサウンドタイプ設定を返す
        
        Returns
        -------
        str
            サウンドタイプ
        """
        return self.sound_type_combo.currentData()