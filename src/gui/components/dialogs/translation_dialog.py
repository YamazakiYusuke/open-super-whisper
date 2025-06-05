"""
翻訳設定を管理するダイアログ

このモジュールは、翻訳機能のON/OFF、翻訳先言語、使用するAIモデルなどの
設定を行うためのダイアログを提供します。
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QCheckBox, QComboBox, QRadioButton,
    QButtonGroup, QGroupBox, QDialogButtonBox
)
from PyQt6.QtCore import Qt, pyqtSignal


class TranslationDialog(QDialog):
    """翻訳設定を管理するダイアログ"""
    
    # 設定変更時のシグナル
    settings_changed = pyqtSignal(dict)
    
    # 利用可能な翻訳先言語
    AVAILABLE_LANGUAGES = [
        ("ja", "日本語"),
        ("en", "英語"),
        ("zh", "中国語（簡体字）"),
        ("zh-TW", "中国語（繁体字）"),
        ("ko", "韓国語"),
        ("es", "スペイン語"),
        ("fr", "フランス語"),
        ("de", "ドイツ語"),
        ("it", "イタリア語"),
        ("pt", "ポルトガル語"),
        ("ru", "ロシア語"),
        ("ar", "アラビア語"),
        ("hi", "ヒンディー語"),
        ("th", "タイ語"),
        ("vi", "ベトナム語"),
        ("id", "インドネシア語"),
        ("tr", "トルコ語"),
        ("pl", "ポーランド語"),
        ("nl", "オランダ語"),
        ("sv", "スウェーデン語"),
    ]
    
    # 翻訳モデルの選択肢
    TRANSLATION_MODELS = [
        {
            "id": "gpt-4o-mini",
            "name": "エコノミー",
            "description": "高速・低コスト",
            "cost": "低",
        },
        {
            "id": "gpt-4o",
            "name": "スタンダード",
            "description": "バランス重視",
            "cost": "中",
        },
        {
            "id": "gpt-4-turbo",
            "name": "プレミアム",
            "description": "最高品質",
            "cost": "高",
        },
    ]
    
    def __init__(self, parent=None, current_settings=None):
        """
        ダイアログの初期化
        
        Parameters
        ----------
        parent : QWidget
            親ウィジェット
        current_settings : dict
            現在の設定値
        """
        super().__init__(parent)
        self.current_settings = current_settings or {}
        self.setup_ui()
        self.load_settings()
        
    def setup_ui(self):
        """UIの構築"""
        self.setWindowTitle("翻訳設定")
        self.setModal(True)
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        
        # 翻訳機能のON/OFFチェックボックス
        self.translation_enabled_checkbox = QCheckBox("翻訳機能を有効にする")
        self.translation_enabled_checkbox.toggled.connect(self.on_translation_toggled)
        layout.addWidget(self.translation_enabled_checkbox)
        
        # 翻訳設定グループ
        self.settings_group = QGroupBox("翻訳設定")
        settings_layout = QVBoxLayout()
        
        # 翻訳先言語の選択
        language_layout = QHBoxLayout()
        language_layout.addWidget(QLabel("翻訳先言語:"))
        self.language_combo = QComboBox()
        for code, name in self.AVAILABLE_LANGUAGES:
            self.language_combo.addItem(name, code)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()
        settings_layout.addLayout(language_layout)
        
        # 翻訳モデルの選択
        model_group = QGroupBox("翻訳モデル")
        model_layout = QVBoxLayout()
        
        self.model_button_group = QButtonGroup()
        for i, model in enumerate(self.TRANSLATION_MODELS):
            radio = QRadioButton()
            radio.setText(f"{model['name']} - {model['description']} (コスト: {model['cost']})")
            radio.setProperty("model_id", model["id"])
            self.model_button_group.addButton(radio, i)
            model_layout.addWidget(radio)
            
            # デフォルトで最初のモデルを選択
            if i == 0:
                radio.setChecked(True)
        
        model_group.setLayout(model_layout)
        settings_layout.addWidget(model_group)
        
        self.settings_group.setLayout(settings_layout)
        layout.addWidget(self.settings_group)
        
        # 注意事項
        info_label = QLabel(
            "※ 翻訳機能を有効にすると、文字起こし後に選択した言語へ自動翻訳されます。\n"
            "※ 翻訳には追加のAPI呼び出しが発生し、コストがかかります。"
        )
        info_label.setWordWrap(True)
        info_label.setStyleSheet("QLabel { color: #666; font-size: 12px; }")
        layout.addWidget(info_label)
        
        # ボタン
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
    def on_translation_toggled(self, checked):
        """翻訳機能のON/OFF切り替え時の処理"""
        self.settings_group.setEnabled(checked)
        
    def load_settings(self):
        """現在の設定を読み込む"""
        # 翻訳機能の有効/無効
        enabled = self.current_settings.get("translation_enabled", False)
        self.translation_enabled_checkbox.setChecked(enabled)
        self.settings_group.setEnabled(enabled)
        
        # 翻訳先言語
        target_language = self.current_settings.get("target_language", "ja")
        index = self.language_combo.findData(target_language)
        if index >= 0:
            self.language_combo.setCurrentIndex(index)
            
        # 翻訳モデル
        model_id = self.current_settings.get("translation_model", "gpt-4o-mini")
        for button in self.model_button_group.buttons():
            if button.property("model_id") == model_id:
                button.setChecked(True)
                break
                
    def get_settings(self):
        """現在の設定を取得"""
        selected_model_button = self.model_button_group.checkedButton()
        model_id = selected_model_button.property("model_id") if selected_model_button else "gpt-4o-mini"
        
        return {
            "translation_enabled": self.translation_enabled_checkbox.isChecked(),
            "target_language": self.language_combo.currentData(),
            "translation_model": model_id,
        }
        
    def accept(self):
        """OKボタンが押された時の処理"""
        self.settings_changed.emit(self.get_settings())
        super().accept()