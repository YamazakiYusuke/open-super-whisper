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
                "ja": "日本語",
                "en": "英語",
                "zh": "中国語（簡体字）",
                "zh-TW": "中国語（繁体字）",
                "ko": "韓国語",
                "es": "スペイン語",
                "fr": "フランス語",
                "de": "ドイツ語",
                "it": "イタリア語",
                "pt": "ポルトガル語",
                "ru": "ロシア語",
                "ar": "アラビア語",
                "hi": "ヒンディー語",
                "th": "タイ語",
                "vi": "ベトナム語",
                "id": "インドネシア語",
                "tr": "トルコ語",
                "pl": "ポーランド語",
                "nl": "オランダ語",
                "sv": "スウェーデン語",
            }
            
            target_language_name = language_names.get(target_language, target_language)
            
            # プロンプトの構築
            if source_language:
                source_language_name = language_names.get(source_language, source_language)
                system_prompt = f"あなたは優秀な翻訳者です。{source_language_name}から{target_language_name}への翻訳を行ってください。"
            else:
                system_prompt = f"あなたは優秀な翻訳者です。与えられたテキストを{target_language_name}に翻訳してください。"
            
            system_prompt += """
翻訳の際は以下の点に注意してください：
- 原文の意味を正確に伝える
- 自然な表現を使用する
- 専門用語は適切に翻訳する
- 文体や敬語レベルは文脈に応じて適切に選択する
- 翻訳結果のみを返し、説明や注釈は含めない
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
            raise Exception(f"翻訳エラー: {str(e)}")