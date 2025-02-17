# Kindle2PDF
このリポジトリは、Kindleデスクトップアプリで表示している本を自動スクリーンショットし、最終的にPDFファイルを生成するツールです。  
**本ツールは個人利用を想定しており、書籍の著作権にご注意のうえ使用してください。**

---

## 概要 (Overview)
- **ドラッグ操作でスクリーンショット領域を指定**  
  コード実行時にポップアップされるウィンドウ上で、マウスドラッグしてキャプチャ範囲を指定できます。  
- **GUI入力でPDFファイル名を指定**  
  起動時にポップアップダイアログが表示され、好きな名前を入力可能です。

---

## 前提条件 (Prerequisites)
- **Python**: 3.XX (最新版で動作確認)  
- **単一ディスプレイ推奨**: マルチディスプレイ環境に対応していないため、トラブルを避けるには単一ディスプレイで利用してください。  
- **Kindleデスクトップアプリ**: 本ツールはKindleアプリを自動操作し、ページ送り等を行います。  
- **Windows環境想定**: win32系のライブラリが必要なため、Windows環境で動作します。

---

## 必要なライブラリ (Required Libraries)

`requirements.txt` に必要なライブラリをまとめてあります。以下のコマンドで一括インストールしてください:

```bash
pip install -r requirements.txt
```

## 使い方 (How to Use)

### Kindleデスクトップアプリを開いて、PDF化したい本を表示しておく

7秒の待機があるので、その間にKindleウィンドウをアクティブにします。

### スクリプトを実行

(例) リポジトリのルートディレクトリで以下を実行:
```bash
python -m kindle2PDF.main
```
もしくは同ディレクトリ内で
```bash
python main.py
```
としても構いません。

---

### GUIダイアログでブックネームを入力
スクリプトを実行すると、まずtkinterのポップアップが表示されます。
保存用フォルダに使う名前を入力してください(キャンセル可能)。

### スクリーンショット領域のドラッグ選択
続いてOpenCVのウィンドウが立ち上がります。
ここでマウスドラッグしてキャプチャしたい領域を選び、Enterキーを押してください。
選択が確定したらウィンドウが閉じます。

### Kindleアプリがアクティブになっているか確認
7秒の待機があるため、その間にKindleアプリをクリックしてアクティブウィンドウにしておいてください。
一度実行されると、指定した領域が自動的にスクリーンショットされます。

### 自動でページ送り・スクショ・PDF生成が行われる
指定した領域の連続スクリーンショットが完了すると、その画像をまとめてPDFファイルに変換します。
PDFは、GUIで入力したフォルダ名＋タイムスタンプのフォルダ内に保存されます。

---

## 注意点
### 座標指定のトラブルについて
マルチディスプレイ環境では予期せぬ座標取得の不具合が起こる可能性があります。
単一ディスプレイを推奨します。

### コード実行中は他の操作をしない
自動的に左矢印キーを押してページを送る仕組みのため、コードの動作中に他のキー操作やウィンドウのアクティブ切り替えを行うと、スクリーンショットが想定外になる可能性があります。

### PDFファイルの扱い
PDF化された書籍の取り扱いには十分配慮してください。
著作権を侵害しない利用方法でお使いください。

### キャンセル動作
GUI入力ダイアログやドラッグ領域選択ウィンドウをキャンセルすると、デフォルト設定またはエラーとなります。
再度スクリプトを実行し直してください。

---

## その他
エラーが発生した場合や領域選択に失敗した場合は、端末を再度単一ディスプレイに設定し直す・Kindleアプリを再起動するなど対処を行ってみてください。
