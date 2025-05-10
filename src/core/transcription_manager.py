from enum import Enum
from src.core.whisper_api import WhisperTranscriber
from src.core.whisper_local import WhisperLocalTranscriber

class TranscriptionMode(Enum):
    """文字起こしモード"""
    API = 0      # API版Whisper
    LOCAL = 1    # ローカル版Whisper

class TranscriptionManager:
    """文字起こしモードを統合管理するクラス"""
    
    def __init__(self, api_key=None):
        """初期化"""
        self.api_transcriber = None
        self.local_transcriber = None
        self.mode = TranscriptionMode.API
        self.api_key = api_key
        
        # APIトランスクライバーの初期化（APIキーがある場合）
        if api_key:
            try:
                self.api_transcriber = WhisperTranscriber(api_key=api_key)
            except ValueError:
                pass
        
        # ローカルトランスクライバーの初期化
        self.local_transcriber = WhisperLocalTranscriber()
    
    def set_api_key(self, api_key):
        """APIキーを設定"""
        self.api_key = api_key
        try:
            self.api_transcriber = WhisperTranscriber(api_key=api_key)
            return True
        except ValueError:
            self.api_transcriber = None
            return False
    
    def set_mode(self, mode):
        """文字起こしモードを設定"""
        if isinstance(mode, int):
            mode = TranscriptionMode(mode)
        self.mode = mode
    
    def get_mode(self):
        """現在のモードを取得"""
        return self.mode
    
    def get_current_transcriber(self):
        """現在のモードに応じたトランスクライバーを取得"""
        if self.mode == TranscriptionMode.API:
            return self.api_transcriber
        else:
            return self.local_transcriber
    
    def set_model(self, model):
        """使用するモデルを設定"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.set_model(model)
    
    def get_available_models(self):
        """現在のモードで利用可能なモデルリストを取得"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            return transcriber.get_available_models()
        return []
    
    def add_custom_vocabulary(self, terms):
        """カスタム語彙を追加"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.add_custom_vocabulary(terms)
    
    def clear_custom_vocabulary(self):
        """カスタム語彙をクリア"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.clear_custom_vocabulary()
    
    def get_custom_vocabulary(self):
        """カスタム語彙を取得"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            return transcriber.get_custom_vocabulary()
        return []
    
    def add_system_instruction(self, instructions):
        """システム指示を追加"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.add_system_instruction(instructions)
    
    def clear_system_instructions(self):
        """システム指示をクリア"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            transcriber.clear_system_instructions()
    
    def get_system_instructions(self):
        """システム指示を取得"""
        transcriber = self.get_current_transcriber()
        if transcriber:
            return transcriber.get_system_instructions()
        return []
    
    def transcribe(self, audio_file, language=None, response_format="text"):
        """音声を文字起こし"""
        transcriber = self.get_current_transcriber()
        if not transcriber:
            return "Error: No transcriber available"
        
        return transcriber.transcribe(audio_file, language, response_format)
    
    def preload_local_model(self, callback=None):
        """ローカルモデルを事前にロード（バックグラウンド）"""
        if self.local_transcriber:
            self.local_transcriber.load_model(callback) 