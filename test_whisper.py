"""
Whisperローカルモードのテスト用スクリプト

Whisperのローカルモードでの文字起こしをテストします。
正常に動作することを確認するため、ffmpegの設定を確認します。
"""

import os
import sys
import whisper
import tempfile

def main():
    """メイン関数"""
    # 設定確認
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Temp directory: {tempfile.gettempdir()}")
    
    # 音声ファイルのパスを指定
    sample_audio = "assets/stop_sound.wav"  # アプリケーションが使用する音声ファイル
    
    # ファイルが存在するか確認
    if not os.path.exists(sample_audio):
        print(f"Error: Audio file not found: {sample_audio}")
        sample_audio = input("Please enter the full path to an audio file: ")
        if not os.path.exists(sample_audio):
            print(f"Error: Audio file not found: {sample_audio}")
            return
    
    print(f"Audio file: {sample_audio}")
    print(f"Absolute path: {os.path.abspath(sample_audio)}")
    
    # Whisperモデルを読み込む
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    
    # 音声を文字起こし
    print("Transcribing audio...")
    try:
        result = model.transcribe(sample_audio)
        print("\nTranscription result:")
        print(result["text"])
    except Exception as e:
        print(f"Transcription error: {e}")
        
    print("\nTest completed.")

if __name__ == "__main__":
    main() 