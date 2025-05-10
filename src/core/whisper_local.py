import tempfile
import threading
import whisper
import numpy as np
import os.path
import shutil  # For file copying operations

class WhisperLocalTranscriber:
    """ローカルWhisperモデルを使用した文字起こしエンジン"""
    
    # 利用可能なモデルサイズ
    AVAILABLE_MODELS = [
        {"id": "tiny", "name": "Tiny (39MB)", "description": "最小・最速モデル、精度は低め"},
        {"id": "base", "name": "Base (142MB)", "description": "バランスの取れた小型モデル"},
        {"id": "small", "name": "Small (466MB)", "description": "バランスの取れた中型モデル"},
        {"id": "medium", "name": "Medium (1.5GB)", "description": "高精度な中型モデル"},
        {"id": "large", "name": "Large (3GB)", "description": "最高精度のモデル"}
    ]
    
    def __init__(self):
        """初期化"""
        self.model = None
        self.model_name = "base"  # デフォルトはbaseモデル
        self.custom_vocabulary = []
        self.system_instructions = []
        self.is_model_loaded = False
        self.loading_thread = None
        
        # 作業ディレクトリの作成
        self.work_dir = os.path.join(tempfile.gettempdir(), "open_super_whisper")
        os.makedirs(self.work_dir, exist_ok=True)
    
    @classmethod
    def get_available_models(cls):
        """利用可能なモデルリストを返す"""
        return cls.AVAILABLE_MODELS
    
    def set_model(self, model_name):
        """使用するモデルを設定"""
        self.model_name = model_name
        self.is_model_loaded = False  # モデル名変更時はロード状態をリセット
    
    def load_model(self, callback=None):
        """
        モデルを非同期でロード
        callback: モデルロード完了時のコールバック関数
        """
        def _load():
            try:
                self.model = whisper.load_model(self.model_name)
                self.is_model_loaded = True
                if callback:
                    callback(True)
            except Exception as e:
                print(f"モデルロードエラー: {e}")
                if callback:
                    callback(False, str(e))
        
        # 既にロードされている場合は何もしない
        if self.is_model_loaded and self.model is not None:
            if callback:
                callback(True)
            return
        
        # 別スレッドでモデルをロード
        self.loading_thread = threading.Thread(target=_load)
        self.loading_thread.daemon = True
        self.loading_thread.start()
    
    def add_custom_vocabulary(self, terms):
        """カスタム語彙を追加"""
        if isinstance(terms, str):
            terms = [terms]
        self.custom_vocabulary.extend(terms)
    
    def clear_custom_vocabulary(self):
        """カスタム語彙をクリア"""
        self.custom_vocabulary = []
    
    def get_custom_vocabulary(self):
        """カスタム語彙を取得"""
        return self.custom_vocabulary
    
    def add_system_instruction(self, instructions):
        """システム指示を追加"""
        if isinstance(instructions, str):
            instructions = [instructions]
        self.system_instructions.extend(instructions)
    
    def clear_system_instructions(self):
        """システム指示をクリア"""
        self.system_instructions = []
    
    def get_system_instructions(self):
        """システム指示を取得"""
        return self.system_instructions
    
    def _build_prompt(self):
        """プロンプトを構築"""
        prompt_parts = []
        
        if self.custom_vocabulary:
            prompt_parts.append("Vocabulary: " + ", ".join(self.custom_vocabulary))
        
        if self.system_instructions:
            prompt_parts.append("Instructions: " + ". ".join(self.system_instructions))
        
        if not prompt_parts:
            return None
            
        return " ".join(prompt_parts)
    
    def transcribe(self, audio_file, language=None, response_format="text"):
        """
        音声を文字起こし
        
        Parameters:
        -----------
        audio_file: str
            音声ファイルのパス
        language: str, optional
            言語コード（ja, en, etc.）
        response_format: str
            応答フォーマット（デフォルト: text）
            
        Returns:
        --------
        str or dict
            文字起こし結果
        """
        # モデルがロードされていなければロード
        if not self.is_model_loaded:
            self.load_model()
            # モデルのロードを待機
            if self.loading_thread and self.loading_thread.is_alive():
                self.loading_thread.join()
            
        if not self.is_model_loaded:
            return "Error: Model not loaded"
        
        try:
            # 元のファイルが存在することを確認
            if not os.path.exists(audio_file):
                raise FileNotFoundError(f"指定されたファイルが見つかりません: {audio_file}")
            
            # 安全な場所にファイルをコピー
            safe_filename = f"input_{os.path.basename(audio_file)}"
            safe_path = os.path.join(self.work_dir, safe_filename)
            
            print(f"音声ファイルをコピー: {audio_file} -> {safe_path}")
            shutil.copy2(audio_file, safe_path)
            
            # コピーされたファイルが存在するか確認
            if not os.path.exists(safe_path):
                raise FileNotFoundError(f"コピー失敗: {safe_path}")
            
            print(f"音声ファイルサイズ: {os.path.getsize(safe_path)} バイト")
            
            # 文字起こしオプションの設定
            options = {
                "fp16": False  # FP16をCPUで使用しない
            }
            
            if language:
                options["language"] = language
            
            # プロンプトがあれば設定
            prompt = self._build_prompt()
            if prompt:
                options["initial_prompt"] = prompt
            
            # 文字起こし実行
            result = self.model.transcribe(safe_path, **options)
            
            # 一時ファイルをクリーンアップ
            try:
                os.remove(safe_path)
            except:
                pass  # クリーンアップ失敗は無視
            
            # フォーマットに応じて結果を返す
            if response_format == "json" or response_format == "verbose_json":
                return result
            else:
                return result["text"]
                
        except Exception as e:
            print(f"文字起こしエラー: {e}")
            return f"Error: {str(e)}" 