# 前提
- ライブラリの関係上、Python 3.13では動きません！
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
- 注意：外部ディスプレイを接続した状態だと座標情報がバグるので、外部ディスプレイを接続していない状態で使用する
- [Kindleデスクトップアプリ](https://www.amazon.co.jp/gp/browse.html?node=26197586051&ref=kcp_fd_hz)をダウンロードして、PDF化したい任意の本を開く
- getPoints.pyをrunさせて、画面の4隅の座標を控える
- 