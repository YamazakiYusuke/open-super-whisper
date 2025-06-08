"""
OpenAI Chat APIを使用した翻訳機能

このモジュールは、文字起こしされたテキストを指定された言語に翻訳する機能を提供します。
"""

import openai
import os


class Translator:
    """OpenAI Chat APIを使用した翻訳クラス"""
    
    def __init__(self, api_key=None):
        """
        翻訳クラスの初期化
        
        Parameters
        ----------
        api_key : str, optional
            OpenAI APIキー。提供されない場合はOPENAI_API_KEY環境変数から取得を試みます。
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError("OpenAI API key is required for translation.")
        
        self.client = openai.OpenAI(api_key=self.api_key)
        
    def translate(self, text, target_language, source_language=None, model="gpt-4o-mini"):
        """
        テキストを指定された言語に翻訳
        
        Parameters
        ----------
        text : str
            翻訳するテキスト
        target_language : str
            翻訳先言語コード（例: "ja", "en", "zh"）
        source_language : str, optional
            元の言語コード。指定しない場合は自動検出
        model : str
            使用するOpenAIモデル
            
        Returns
        -------
        str
            翻訳されたテキスト
        """
        try:
            # 言語名のマッピング
            language_names = {
                "ja": "Japanese",
                "en": "English",
                "zh": "Chinese (Simplified)",
                "zh-TW": "Chinese (Traditional)",
                "ko": "Korean",
                "es": "Spanish",
                "fr": "French",
                "de": "German",
                "it": "Italian",
                "pt": "Portuguese",
                "ru": "Russian",
                "ar": "Arabic",
                "hi": "Hindi",
                "th": "Thai",
                "vi": "Vietnamese",
                "id": "Indonesian",
                "tr": "Turkish",
                "pl": "Polish",
                "nl": "Dutch",
                "sv": "Swedish",
            }
            
            target_language_name = language_names.get(target_language, target_language)
            
            # プロンプトの構築
            if source_language:
                source_language_name = language_names.get(source_language, source_language)
                system_prompt = f"You are an excellent translator. Please translate from {source_language_name} to {target_language_name}."
            else:
                system_prompt = f"You are an excellent translator. Please translate the given text to {target_language_name}."
            
            system_prompt += """
Please pay attention to the following points when translating:
- Accurately convey the meaning of the original text
- Use natural expressions
- Translate technical terms appropriately
- Choose appropriate style and formality level according to context
- Return only the translation result without explanations or annotations
"""
            
            # Chat APIを呼び出し
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                temperature=0.3,  # より一貫性のある翻訳のため低めに設定
                max_tokens=4000,
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Translation error: {e}")
            raise Exception(f"Translation error: {str(e)}")