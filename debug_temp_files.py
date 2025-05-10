"""
一時ファイルのデバッグスクリプト

このスクリプトは一時ディレクトリのファイルをリストアップし、
オーディオファイルの存在と文字起こしの可能性を確認します。
"""

import os
import tempfile
import glob
import datetime

def main():
    """メイン関数"""
    # 一時ディレクトリを取得
    temp_dir = tempfile.gettempdir()
    print(f"一時ディレクトリ: {temp_dir}")
    
    # 一時ディレクトリの録音ファイルを検索
    recording_files = glob.glob(os.path.join(temp_dir, "recording_*.wav"))
    
    # 時間順にソート
    recording_files.sort(key=os.path.getmtime, reverse=True)
    
    print(f"見つかった録音ファイル数: {len(recording_files)}\n")
    
    # 各ファイルの情報を表示
    for i, file_path in enumerate(recording_files[:10], 1):  # 最新10件のみ表示
        file_size = os.path.getsize(file_path) / 1024  # KB単位に変換
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        
        print(f"{i}. ファイル: {os.path.basename(file_path)}")
        print(f"   - 絶対パス: {os.path.abspath(file_path)}")
        print(f"   - サイズ: {file_size:.2f} KB")
        print(f"   - 最終更新: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   - 存在確認: {'はい' if os.path.exists(file_path) else 'いいえ'}")
        
        # ファイルが正常に読み取り可能か確認
        try:
            with open(file_path, 'rb') as f:
                # 最初の数バイトのみ読み取り
                header = f.read(12)
                print(f"   - 読み取り: {'成功' if header else '失敗'}")
        except Exception as e:
            print(f"   - 読み取りエラー: {e}")
        
        print()
    
    # 手動テスト用の指示
    if recording_files:
        print("\n最新の録音ファイルをテストするには、以下のコマンドを実行してください:")
        print(f"python test_whisper.py {os.path.abspath(recording_files[0])}")
    
if __name__ == "__main__":
    main() 