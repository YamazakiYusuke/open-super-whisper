# Open Super Whisper

<img src="assets/icon.png" alt="Open Super Whisper アイコン" width="128" height="128" align="right"/>

グローバルホットキー制御による簡単な音声文字起こしデスクトップアプリケーション。録音、文字起こし、貼り付けがアプリケーションを切り替えることなく行えます。

## クイックスタート - たった3ステップ！

1. **録音開始** - どのアプリケーションからでもグローバルホットキー（デフォルト：Ctrl+Shift+R）を押します
2. **録音停止** - 話し終わったら同じホットキーをもう一度押します
3. **テキスト貼り付け** - 文字起こし結果は自動的にクリップボードにコピーされるので、必要な場所に貼り付けるだけです

これだけです！作業の流れを中断することなく文字起こしが完了します。

## 特徴

- 🎙️ マイクから直接音声を録音
- 🌎 自動言語検出機能付きで100以上の言語をサポート
- 📝 文字起こし精度を向上させるカスタム語彙機能
- 🔧 文字起こしの動作をコントロールするシステム指示機能
- 📋 クリップボードに文字起こし内容をコピー
- 🔄 リアルタイムの録音状態表示とタイマー
- 💻 OpenAI APIとローカルWhisperモデルの両方をサポート

## 利用可能なモデル

Open Super Whisperでは2つの文字起こしモードを利用できます：

### OpenAI APIモデル

- **Whisper-1** - OpenAIのオリジナルオープンソースWhisperモデル
- **GPT-4o Transcribe** - 高性能文字起こしモデルで、優れた精度を提供
- **GPT-4o Mini Transcribe** - 軽量・高速な文字起こしモデルで、速度と精度のバランスに優れています

### ローカルWhisperモデル

APIキー不要！コンピュータ上で直接Whisperモデルを使用できます：

- **Tiny (39MB)** - 最小・最速モデル、精度は低め
- **Base (142MB)** - バランスの取れた小型モデル
- **Small (466MB)** - バランスの取れた中型モデル
- **Medium (1.5GB)** - 高精度な中型モデル
- **Large (3GB)** - 最高精度のモデル

ローカルモデルはシステムリソースを多く必要としますが、インターネット接続やAPI費用が不要になります。

## デモ

![Open Super Whisperの動作デモ](demo/demo.gif)

## ダウンロード

Windows用の最新の実行可能ファイル（.exe）は、[GitHub Releasesページ](https://github.com/TakanariShimbo/open-super-whisper/releases)からダウンロードできます。

## 必要条件

- APIモード用：OpenAI APIキー
- ローカルモード用：システムにインストールされたFFmpeg
- WindowsまたはmacOSオペレーティングシステム

## インストール方法

### ローカルWhisperモードの追加セットアップ

ローカルWhisperモデルを使用するには、FFmpegをインストールする必要があります：

#### Windows
```bash
# wingetを使用
winget install -e --id Gyan.FFmpeg

# または公式サイトからダウンロード
# https://ffmpeg.org/download.html
```

#### macOS
```bash
# Homebrewを使用
brew install ffmpeg
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

### UV を使用した方法

[UV](https://github.com/astral-sh/uv)は高速で効率的なPythonパッケージインストーラーおよび環境マネージャーです。従来のpipやvenvよりも高速で、依存関係の解決も優れています。

1. UVがインストールされているか確認：

```bash
uv --version
```

2. インストールされていない場合は、次のコマンドでインストールできます：

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. リポジトリをクローンまたはダウンロード

4. UVのsyncコマンドを使用してプロジェクトをセットアップ（仮想環境の作成と依存関係のインストールを自動的に行います）：

```bash
uv sync
```

5. 仮想環境をアクティベート：

```bash
# Windows (PowerShell)
.\.venv\Scripts\activate.ps1

# macOS/Linux の場合
source .venv/bin/activate
```

> **注意**: PowerShellで`activate.ps1`実行時に「このシステムではスクリプトの実行が無効になっている」というエラーが表示される場合は、以下のいずれかの方法を試してください：
> 
> 1. コマンドプロンプト（cmd.exe）を使用して`.venv\Scripts\activate.bat`を実行
> 2. PowerShellで以下のコマンドを実行して、現在のセッションのみ実行ポリシーを変更:
>    ```powershell
>    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
>    ```
>    その後、`.\.venv\Scripts\activate.ps1`を実行
> 3. 管理者権限でPowerShellを実行し、ユーザーアカウントの実行ポリシーを変更（セキュリティ上のリスクを理解した上で行ってください）:
>    ```powershell
>    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>    ```

6. アプリケーションを実行：

```bash
python main.py
```

### アプリケーションのビルド方法

スタンドアロンの実行可能ファイルを作成するには、PyInstallerを使用します：

```bash
# Windows (PowerShell)
python -m PyInstaller --onefile --windowed --icon assets/icon.ico --name "OpenSuperWhisper" --add-data "assets;assets" main.py

# macOS の場合
python -m PyInstaller --onefile --windowed --icon assets/icon.icns --name "OpenSuperWhisper" --add-data "assets:assets" main.py

# Linux の場合
python -m PyInstaller --onefile --windowed --icon assets/linux_pngs/icon_256.png --name "OpenSuperWhisper" --add-data "assets:assets" main.py
```


最初のコマンドは以下の処理を行います：
- `--onefile`: 単一の実行可能ファイルを作成
- `--windowed`: コンソールウィンドウを表示しない
- `--icon assets/icon.ico`: アプリケーションアイコンを設定
- `--name "OpenSuperWhisper"`: 出力ファイル名を指定
- `--add-data "assets;assets"`: assetsディレクトリを実行可能ファイルに含める

ビルドが完了すると、Windowsでは`dist`フォルダ内に`OpenSuperWhisper.exe`、macOSでは`dist`フォルダ内に`OpenSuperWhisper.app`が生成されます。

## 使用方法

### 文字起こしモードの選択

1. 「文字起こしモード」ドロップダウンから「OpenAI API」または「ローカルモデル」を選択
2. APIモードでは、OpenAI APIキーが必要です
3. ローカルモードでは、様々なモデルサイズから選択可能
   - 小さいモデルは高速ですが精度は低め
   - 大きいモデルは精度が高いがメモリと処理能力をより多く必要とします
4. ローカルモデルを初めて使用する場合、自動的にダウンロードされます

### APIキーの設定（APIモード用）

1. APIモードで初回起動時にOpenAI APIキーの入力が求められます
2. APIキーをお持ちでない場合は、[OpenAIのウェブサイト](https://platform.openai.com/api-keys)から取得できます
3. APIキーは今後の使用のために保存されます
4. 後で変更する場合は、ツールバーの「APIキー設定」をクリックします
5. ローカルモードでは不要です

### 音声の録音

1. 「録音開始」ボタンをクリックしてマイクからの録音を開始
2. 「録音停止」をクリックして録音を終了
3. アプリケーションは自動的に録音内容を文字起こしします
4. グローバルホットキー（デフォルト: Ctrl+Shift+R）を使用して、アプリケーションがバックグラウンドにある場合でも録音の開始/停止が可能です

### グローバルホットキーの使用

1. デフォルトのホットキーは「Ctrl+Shift+R」に設定されています
2. このホットキーを押すと、アプリケーションがバックグラウンドにあっても録音を開始/停止できます
3. ホットキーを変更するには、ツールバーの「ホットキー設定」をクリックします

### システムトレイ（Windows）またはメニューバー（macOS）の活用

1. アプリケーションはシステムトレイ（Windows）またはメニューバー（macOS）に常駐します
2. ウィンドウを閉じてもアプリケーションはバックグラウンドで実行され続けます
3. システムトレイ/メニューバーアイコンをクリックしてアプリケーションの表示/非表示を切り替えます
4. システムトレイアイコンを右クリック（Windows）またはメニューバーアイコンをクリック（macOS）して以下の操作が可能です：
   - アプリケーションの表示
   - 録音の開始/停止
   - アプリケーションの完全終了

### 言語選択

1. 録音前に、ドロップダウンメニューから言語を選択
2. 「自動検出」を選択すると、Whisperが自動的に言語を識別します

### モデル選択

1. ドロップダウンメニューから使用するモデルを選択できます
2. 各モデルは精度と処理速度のバランスが異なります
3. 選択したモデルは次回使用時も保持されます
4. ローカルモードの場合、メモリ要件に注意：
   - Tiny: 約39MB RAM
   - Base: 約142MB RAM
   - Small: 約466MB RAM
   - Medium: 約1.5GB RAM
   - Large: 約3GB RAM

### カスタム語彙

1. ツールバーの「カスタム語彙」をクリック
2. 音声に含まれる可能性のある特定の用語、名前、フレーズを追加
3. これらの用語は文字起こしの精度向上に役立ちます

### システム指示

1. ツールバーの「システム指示」をクリック
2. 文字起こしの動作をコントロールするための指示を追加できます：
   - 「えー、あの、などのフィラーを無視する」
   - 「適切な句読点を追加する」
   - 「テキストを段落に分ける」
3. これらの指示により、手動編集なしで洗練された文字起こし結果が得られます

### 文字起こし結果の管理

1. メインテキストエリアで文字起こし結果を表示
2. 必要に応じてテキストを編集（テキストエリアは編集可能）
3. ツールバーのボタンを使用して：
   - クリップボードに文字起こしをコピー

### その他の設定

1. 「自動コピー」オプション：文字起こし完了時に自動的にクリップボードにコピーする機能をオン/オフできます

### コマンドラインオプション

アプリケーションは以下のコマンドライン引数をサポートしています：

```bash
python main.py -m
# または
python main.py --minimized
```

`-m`または`--minimized`オプションを使用すると、アプリケーションはシステムトレイのみに起動し、ウィンドウは表示されません。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています - 詳細はLICENSEファイルをご覧ください。

## 謝辞

- このアプリケーションは[OpenAIのWhisper API](https://platform.openai.com/docs/guides/speech-to-text)および[Whisperオープンソースモデル](https://github.com/openai/whisper)を音声認識に使用しています
- ユーザーインターフェースは[PyQt6](https://www.riverbankcomputing.com/software/pyqt/)で構築されています
- [Super Whisper](https://superwhisper.com/)デスクトップアプリケーションに触発されています
