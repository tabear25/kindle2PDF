import pyautogui
import win32gui
import win32ui
import win32con
import win32api
import time
import os
import datetime
from PIL import Image
from fpdf import FPDF

# スクリーンショットを取得したい範囲の座標
left, top, width, height = (50, 120, 1080, 1355)
# スクショ間隔(秒)
span = 1
# 作成するフォルダ名を指定します。
# PDFファイル名にもなります。
h_foldername = "40字要約で仕事はどんどんうまくいく"
# 出力ファイル頭文字
h_filename = "Page"

# 7秒の間に、スクショしたいkindleの画面に移動
time.sleep(7)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

# スクショ処理
prev_img = None
same_cnt = 0
p = 0
while True:
    # アクティブなウィンドウのハンドルを取得する
    handle = win32gui.GetForegroundWindow()
    # デバイスコンテキストを作成する
    hwindc = win32gui.GetWindowDC(handle)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    # ビットマップオブジェクトを作成する
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    # スクリーンショットを取得する
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    # ビットマップを画像に変換する
    bmpinfo = bmp.GetInfo()
    bmpstr = bmp.GetBitmapBits(True)
    s = Image.frombuffer(
        "RGB",
        (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
        bmpstr,
        "raw",
        "BGRX",
        0,
        1,
    )
    # デバイスコンテキストを解放する
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(handle, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    p = p + 1
    # 前回の画像と同じか判定
    if prev_img is None or not s.tobytes() == prev_img.tobytes():
        # 前回の画像と異なる場合はスクリーンショットを保存
        out_filename = h_filename + "_" + str(p).zfill(4) + '.png'
        s.save(folder_name + "/" + out_filename)
        prev_img = s
        same_cnt = 0
        # 次のページ
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        # 画面の動作待ち
        time.sleep(span)
    else:
        # 前回の画像と同じ場合はカウンタを増やす
        same_cnt += 1

    # 3回同じ画像が出現した場合は終了
    if same_cnt >= 3:
        break

    # 処理中のページ番号を画面に出力
    print(f"Processing page {p}")

# 画像をPDFにまとめる
pdf = FPDF()

for filename in sorted(os.listdir(folder_name)):
    if filename.endswith('.png'):
        img_path = os.path.join(folder_name, filename)
        cover = Image.open(img_path)
        width, height = cover.size
        
        # Convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)
        
        # given we are working with A4 format size 
        pdf_size = {'P': (210, 297), 'L': (297, 210)}
        
        # get page orientation from image size 
        orientation = 'P' if width < height else 'L'
        
        #  make sure image size is not greater than the pdf format size 
        width = width if width < pdf_size[orientation][0] else pdf_size[orientation][0]
        height = height if height < pdf_size[orientation][1] else pdf_size[orientation][1]
        
        pdf.add_page(orientation = orientation)
        pdf.image(img_path, 0, 0, width, height)

# 保存するPDFのファイル名
pdf_output = folder_name + ".pdf"
pdf.output(pdf_output, "F")

print(f"PDF file {pdf_output} created successfully.")
