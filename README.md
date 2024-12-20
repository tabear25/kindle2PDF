# main
Convert Kindle books into PDF format

# 前提条件（Prerequisites）

このツールを使用する前に、以下の条件を理解しておいてください：

- **Pythonのバージョン**: 最新版までの動作確認済みです。
- **マルチディスプレイ環境**: このシステムはマルチディスプレイ（複数のモニター）時の座標の再設定を機能として実装していないので単一ディスプレイで使用してください。

## 必要なライブラリ（Required Libraries）
`requirements.txt`にまとめてあるので全てインストールしてください

# 使い方（How to Use）

### 1. 準備（Preparation）

1. **Kindleデスクトップアプリを開く**
   - [Kindleデスクトップアプリ](https://www.amazon.co.jp/gp/browse.html?node=26197586051&ref=kcp_fd_hz)をダウンロードして、PDF化したい任意の本を開いた状態にしてください。

2. **getPoints.pyで座標を取得**
   - スクリーンショットを取得する範囲を決定するため、`getPoints.py` を実行してKindleデスクトップアプリの4隅の座標をメモします。
   - スクリーンショットを取得する範囲にはウィンドウの×ボタンなどバーに該当する部分は含まないようにしてください。
   - 座標の計測が完了したら、ターミナルにカーソルを合わせて `Ctrl+C` で終了してください。

### 2. PDF化する（Convert to PDF）

1. **main.pyの設定**
   - `main.py` ファイルを編集し、以下の変数に先ほど取得した座標を入力します。
   
   ```python
   left, top, width, height = (, , , )
   ```

   - 各項目について、以下の表を参考にしてください：

   | 項目  | 説明 |
   |-------|------|
   | left  | 4隅において左辺に該当する座標のx軸 |
   | top   | 4隅において左上に該当する座標のy軸 |
   | width | x軸を右辺 - 左辺した値 |
   | height| y軸を上端 - 下端した値 |

2. **フォルダ名を設定する**
   - PDFファイルが保存されるフォルダ名を指定します。
   
   ```python
   h_foldername = "YOUR_BOOKNAME"
   ```
   - `"YOUR_BOOKNAME"` の部分を、任意のファイル名に置き換えてください。この名前は作成されるPDFファイルの保存先フォルダになります。

3. **実行する（Run the Script）**
   - 全ての設定が完了したら、スクリプトをrunします。
   - 実行してから **7秒以内にKindleデスクトップアプリをアクティブなウィンドウ** にする必要があります。マウスを使ってKindleウィンドウをクリックしてアクティブなウィンドウに設定してください。
   - その後、指定した座標内でのアクティブなウィンドウでスクリーンショットが自動で行われるため、スクリプトが完了するまで **他の操作を行わないでください**。PCがスリープしたりしてもいけないので、予めスリープ設定をオフにしておくことをお勧めします。

### 注意点（Notes）

- スクリーンショットを撮るために、スクリーンの特定の部分を正確に指定する必要があります。そのため、座標を取得する際には正確に4隅を計測・メモするようにしてください。
- 作業中にPCで他の操作を行うと、スクリーンショットが正しく取得できない可能性があります。コードの実行中は他の操作を控えてください。
- 最後にPDFファイルが生成されます。生成されたPDFファイルは指定したフォルダ内にPDFで保存されます。保存されるファイル名はファイルが作成された日付になります。