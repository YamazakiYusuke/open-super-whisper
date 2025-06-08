from src.core.whisper_api import WhisperTranscriber
from src.core.translator import Translator

class TranscriptionManager:
    """API文字起こしを管理するクラス"""
    
    def __init__(self, api_key=None):
        """初期化"""
        self.api_transcriber = None
        self.translator = None
        self.api_key = api_key
        
        # 翻訳設定
        self.translation_enabled = False
        self.target_language = "ja"
        self.translation_model = "gpt-4o-mini"
        
        # APIトランスクライバーの初期化（APIキーがある場合）
        if api_key:
            try:
                self.api_transcriber = WhisperTranscriber(api_key=api_key)
                self.translator = Translator(api_key=api_key)
            except ValueError:
                pass
    
    def set_api_key(self, api_key):
        """APIキーを設定"""
        self.api_key = api_key
        try:
            self.api_transcriber = WhisperTranscriber(api_key=api_key)
            self.translator = Translator(api_key=api_key)
            return True
        except ValueError:
            self.api_transcriber = None
            self.translator = None
            return False
    
    def get_current_transcriber(self):
        """APIトランスクライバーを取得"""
        return self.api_transcriber
    
    def set_model(self, model):
        """使用するモデルを設定"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.set_model(model)
    
    def get_available_models(self):
        """利用可能なAPIモデルリストを取得"""
        if self.api_transcriber:
            return self.api_transcriber.get_available_models()
        return []
    
    def add_custom_vocabulary(self, terms):
        """カスタム語彙を追加"""
        if self.api_transcriber:
            self.api_transcriber.add_custom_vocabulary(terms)
    
    def clear_custom_vocabulary(self):
        """カスタム語彙をクリア"""
        if self.api_transcriber:
            self.api_transcriber.clear_custom_vocabulary()
    
    def get_custom_vocabulary(self):
        """カスタム語彙を取得"""
        if self.api_transcriber:
            return self.api_transcriber.get_custom_vocabulary()
        return []
    
    def add_system_instruction(self, instructions):
        """システム指示を追加"""
        if self.api_transcriber:
            self.api_transcriber.add_system_instruction(instructions)
    
    def clear_system_instructions(self):
        """システム指示をクリア"""
        if self.api_transcriber:
            self.api_transcriber.clear_system_instructions()
    
    def get_system_instructions(self):
        """システム指示を取得"""
        if self.api_transcriber:
            return self.api_transcriber.get_system_instructions()
        return []
    
    def transcribe(self, audio_file, language=None, response_format="text"):
        """音声を文字起こし"""
        if not self.api_transcriber:
            return "Error: No API transcriber available"
        
        return self.api_transcriber.transcribe(audio_file, language, response_format)
    
    def set_translation_enabled(self, enabled):
        """翻訳機能の有効/無効を設定"""
        self.translation_enabled = enabled
    
    def is_translation_enabled(self):
        """翻訳機能が有効かどうかを取得"""
        return self.translation_enabled
    
    def set_target_language(self, language):
        """翻訳先言語を設定"""
        self.target_language = language
    
    def get_target_language(self):
        """翻訳先言語を取得"""
        return self.target_language
    
    def set_translation_model(self, model):
        """翻訳モデルを設定"""
        self.translation_model = model
    
    def get_translation_model(self):
        """翻訳モデルを取得"""
        return self.translation_model
    
    def translate(self, text, source_language=None):
        """テキストを翻訳"""
        if not self.translation_enabled or not self.translator:
            return None
        
        try:
            return self.translator.translate(
                text=text,
                target_language=self.target_language,
                source_language=source_language,
                model=self.translation_model
            )
        except Exception as e:
            print(f"Translation error: {e}")
            return f"翻訳エラー: {str(e)}"
    
    def transcribe_and_translate(self, audio_file, language=None, response_format="text"):
        """音声を文字起こしし、必要に応じて翻訳"""
        # まず文字起こしを実行
        transcription = self.transcribe(audio_file, language, response_format)
        
        # 翻訳が有効な場合は翻訳も実行
        translation = None
        if self.translation_enabled and transcription and not transcription.startswith("Error"):
            translation = self.translate(transcription, language)
        
        return {
            "transcription": transcription,
            "translation": translation
        } 