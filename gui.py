import tkinter as tk
from tkinter import simpledialog

def get_book_name():
    root = tk.Tk()
    root.withdraw()  

    # ダイアログ表示
    book_name = simpledialog.askstring("Book Name", "Enter your book name:")

    root.destroy()
    return book_name

if __name__ == "__main__":
    name = get_book_name()
    if name:
        print(f"以下の名前でPDFファイルを保存します: {name}")
    else:
        print("ブックネームの入力がキャンセルされました。")