import os
import time
import datetime
import pyautogui
import cv2
import numpy as np
from PIL import Image
from fpdf import FPDF
from capture_region import select_region
from gui import get_book_name  

# Kindleウィンドウに移動するための待機時間
time.sleep(7)

# スクリーンショットを撮影する機能
screenshot = pyautogui.screenshot()
img_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# ROIを選択
left, top, width, height = select_region(img_cv)
print(f"選択された領域: left={left}, top={top}, width={width}, height={height}")

# 保存用のフォルダ作成
h_foldername = get_book_name() or "DefaultBookName" 
folder_name = h_foldername + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
os.mkdir(folder_name)

prev_img = None
same_cnt = 0
p = 0
# キー操作後の待機秒数
span = 1  

while True:
    # 現在アクティブなウィンドウを取得
    handle = pyautogui.getActiveWindow()  
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    s = screenshot.convert("RGB")
    
    p += 1
    if prev_img is None or s.tobytes() != prev_img.tobytes():
        out_filename = f"Page_{str(p).zfill(4)}.png"
        s.save(os.path.join(folder_name, out_filename))
        prev_img = s
        same_cnt = 0
        
        # ページをめくる機能（左に次のページが進む想定）
        pyautogui.press('left')
        """
        洋書など右に次のページが進む場合は以下のコードを利用
        pyautogui.press('right')
        """
        time.sleep(span)
    else:
        same_cnt += 1

    if same_cnt >= 3: # 見開き空白で処理が止まることを防ぐため3ページ同じページが連続したら処理を停止
        break

    print(f"Processing page {p}")

# 作成したスクショをPDFに変換する
pdf = FPDF()

for filename in sorted(os.listdir(folder_name)):
    if filename.endswith('.png'):
        img_path = os.path.join(folder_name, filename)
        cover = Image.open(img_path)
        w, h = cover.size
        w, h = float(w * 0.264583), float(h * 0.264583)
        
        pdf_size = {'P': (210, 297), 'L': (297, 210)}
        orientation = 'P' if w < h else 'L'
        w = w if w < pdf_size[orientation][0] else pdf_size[orientation][0]
        h = h if h < pdf_size[orientation][1] else pdf_size[orientation][1]
        
        pdf.add_page(orientation=orientation)
        pdf.image(img_path, 0, 0, w, h)

pdf_output = folder_name + ".pdf"
pdf.output(pdf_output, "F")

print(f"PDF file {pdf_output} created successfully.")