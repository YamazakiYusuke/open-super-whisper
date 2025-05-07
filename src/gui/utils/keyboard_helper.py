"""
キーボード自動化ユーティリティモジュール

クリップボードのテキストを現在アクティブなテキストフィールドにペーストするための
キーボード自動化機能を提供します。
"""

import time
from pynput.keyboard import Key, Controller

class KeyboardAutomation:
    """
    キーボード入力を自動化するクラス
    
    このクラスは、pynputライブラリを使用してキーボード入力を自動化し、
    クリップボードのテキストをアクティブなテキストフィールドにペーストするための
    機能を提供します。
    """
    
    def __init__(self):
        """KeyboardAutomationの初期化"""
        self.keyboard = Controller()
    
    def paste_clipboard_content(self):
        """
        クリップボードの内容をアクティブなフィールドにペーストする
        
        現在アクティブなアプリケーションの入力フィールドに
        クリップボードの内容をペーストします（Ctrl+V相当の操作）。
        """
        # 少し待機してアプリケーションが切り替わる時間を確保
        time.sleep(0.5)
        
        # Ctrl+V（Windows/Linux）または Command+V（macOS）を送信
        try:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press('v')
                self.keyboard.release('v')
        except Exception as e:
            print(f"自動ペースト中にエラーが発生しました: {str(e)}")
    
    @staticmethod
    def get_instance():
        """シングルトンインスタンスを取得"""
        if not hasattr(KeyboardAutomation, "_instance"):
            KeyboardAutomation._instance = KeyboardAutomation()
        return KeyboardAutomation._instance 