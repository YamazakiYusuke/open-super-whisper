#!/usr/bin/env python3
"""
翻訳機能のコアロジックテスト

GUI依存部分を除いた翻訳機能のテストです。
"""

import sys
import os

# プロジェクトのパスを追加
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_translator_import():
    """翻訳クラスのインポートテスト"""
    try:
        from src.core.translator import Translator
        print("✅ Translator クラスのインポート成功")
        return True
    except ImportError as e:
        print(f"❌ Translator クラスのインポート失敗: {e}")
        return False

def test_transcription_manager_import():
    """TranscriptionManager のインポートテスト"""
    try:
        from src.core.transcription_manager import TranscriptionManager
        print("✅ TranscriptionManager クラスのインポート成功")
        return True
    except ImportError as e:
        print(f"❌ TranscriptionManager クラスのインポート失敗: {e}")
        return False

def test_translator_init():
    """翻訳クラスの初期化テスト（モックAPIキー使用）"""
    try:
        from src.core.translator import Translator
        
        # モックAPIキーでテスト
        translator = Translator(api_key="test-key")
        print("✅ Translator クラスの初期化成功")
        return True
    except Exception as e:
        print(f"❌ Translator クラスの初期化失敗: {e}")
        return False

def test_transcription_manager_init():
    """TranscriptionManager の初期化テスト"""
    try:
        from src.core.transcription_manager import TranscriptionManager
        
        # モックAPIキーでテスト
        manager = TranscriptionManager(api_key="test-key")
        print("✅ TranscriptionManager クラスの初期化成功")
        return True
    except Exception as e:
        print(f"❌ TranscriptionManager クラスの初期化失敗: {e}")
        return False

def test_translation_settings():
    """翻訳設定のテスト"""
    try:
        from src.core.transcription_manager import TranscriptionManager
        
        manager = TranscriptionManager(api_key="test-key")
        
        # 翻訳設定をテスト
        manager.set_translation_enabled(True)
        assert manager.is_translation_enabled() == True
        
        manager.set_target_language("ja")
        assert manager.get_target_language() == "ja"
        
        manager.set_translation_model("gpt-4o-mini")
        assert manager.get_translation_model() == "gpt-4o-mini"
        
        print("✅ 翻訳設定のテスト成功")
        return True
    except Exception as e:
        print(f"❌ 翻訳設定のテスト失敗: {e}")
        return False

def test_config_constants():
    """設定定数の追加テスト"""
    try:
        from src.gui.resources.config import AppConfig
        
        # 新しく追加した設定項目をチェック
        assert hasattr(AppConfig, 'DEFAULT_TRANSLATION_ENABLED')
        assert hasattr(AppConfig, 'DEFAULT_TARGET_LANGUAGE')  
        assert hasattr(AppConfig, 'DEFAULT_TRANSLATION_MODEL')
        
        # デフォルト値をチェック
        assert AppConfig.DEFAULT_TRANSLATION_ENABLED == False
        assert AppConfig.DEFAULT_TARGET_LANGUAGE == "ja"
        assert AppConfig.DEFAULT_TRANSLATION_MODEL == "gpt-4o-mini"
        
        print("✅ 設定定数の追加テスト成功")
        return True
    except Exception as e:
        print(f"❌ 設定定数の追加テスト失敗: {e}")
        return False

def test_translation_models():
    """翻訳モデルの定義テスト"""
    try:
        from src.gui.components.dialogs.translation_dialog import TranslationDialog
        
        # 翻訳モデルの定義をチェック
        models = TranslationDialog.TRANSLATION_MODELS
        assert len(models) == 3  # エコノミー、スタンダード、プレミアム
        
        # 各モデルの構造をチェック
        for model in models:
            assert "id" in model
            assert "name" in model
            assert "description" in model
            assert "cost" in model
        
        # 特定のモデルをチェック
        model_ids = [model["id"] for model in models]
        assert "gpt-4o-mini" in model_ids
        assert "gpt-4o" in model_ids
        assert "gpt-4-turbo" in model_ids
        
        print("✅ 翻訳モデルの定義テスト成功")
        return True
    except Exception as e:
        print(f"❌ 翻訳モデルの定義テスト失敗: {e}")
        return False

def test_translate_method():
    """翻訳メソッドのテスト（実際のAPI呼び出しなし）"""
    try:
        from src.core.transcription_manager import TranscriptionManager
        
        manager = TranscriptionManager(api_key="test-key")
        manager.set_translation_enabled(True)
        manager.set_target_language("ja")
        manager.set_translation_model("gpt-4o-mini")
        
        # 翻訳機能が無効の場合
        manager.set_translation_enabled(False)
        result = manager.translate("Hello, world!")
        assert result is None
        
        print("✅ 翻訳メソッドのテスト成功")
        return True
    except Exception as e:
        print(f"❌ 翻訳メソッドのテスト失敗: {e}")
        return False

def main():
    """メインテスト関数"""
    print("🧪 翻訳機能のコアロジックテストを開始します...\n")
    
    tests = [
        test_translator_import,
        test_transcription_manager_import,
        test_translator_init,
        test_transcription_manager_init,
        test_translation_settings,
        test_config_constants,
        test_translation_models,
        test_translate_method,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ テスト実行中にエラー: {e}")
        print()
    
    print(f"📊 テスト結果: {passed}/{total} 通過")
    
    if passed == total:
        print("🎉 すべてのテストが通過しました！")
        return 0
    else:
        print("⚠️  一部のテストが失敗しました。")
        return 1

if __name__ == "__main__":
    sys.exit(main())