# kindle2PDF
Make PDF version of kindle books

# 前提
- ライブラリの関係上、最新版のPython 3.13では動きません！
- 開発は [3.12.6](https://www.python.org/downloads/release/python-3126/)でしたので、特段のこだわりが無い限り、3.12.6での使用をお勧めします。

## 使用するライブラリ
- 以下のライブラリをインストール
- [win32gui](https://pypi.org/project/win32gui/)
- [time](https://pypi.org/project/TIME-python/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [os-sys](https://pypi.org/project/os-sys/)
- [DateTime](https://pypi.org/project/DateTime/)
- [PIL](https://pypi.org/project/pillow/)
- [fpdf](https://pypi.org/project/fpdf/)

# 使い方
### 準備
- 注意：外部ディスプレイを接続した状態だと座標情報がバグるので、外部ディスプレイを接続していない状態で使用する
- [Kindleデスクトップアプリ](https://www.amazon.co.jp/gp/browse.html?node=26197586051&ref=kcp_fd_hz)をダウンロードして、PDF化したい任意の本を開く
### PDF化する範囲を決定する
- getPoints.pyをrunさせて、画面の4隅の座標をメモしておく
- 計測が完了したらターミナルにカーソルを合わせて Ctrl+Cで終了する
### PDF化する
- Kindle2PDF.pyを用いてPDF化する
- 'left, top, width, height = (, , , )'にgetPoints.pyで控えた座標を記入する
｜left｜4隅において左辺に該当する座標のx軸｜
｜top｜4隅において左上に該当する座標のy軸｜
｜width｜x軸を右辺 - 左辺した値｜
｜height｜y軸を上端 - 下端した値｜
- 