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

left, top, width, height = (, , , )
span = 1
h_foldername = "YOUR_BOOKNAME"
h_filename = "Page"

time.sleep(7)

folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

prev_img = None
same_cnt = 0
p = 0
while True:
    handle = win32gui.GetForegroundWindow()
    hwindc = win32gui.GetWindowDC(handle)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
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

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(handle, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    p = p + 1
    if prev_img is None or not s.tobytes() == prev_img.tobytes():
        out_filename = h_filename + "_" + str(p).zfill(4) + '.png'
        s.save(folder_name + "/" + out_filename)
        prev_img = s
        same_cnt = 0
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        time.sleep(span)
    else:
        same_cnt += 1

    if same_cnt >= 3:
        break

    print(f"Processing page {p}")

pdf = FPDF()

for filename in sorted(os.listdir(folder_name)):
    if filename.endswith('.png'):
        img_path = os.path.join(folder_name, filename)
        cover = Image.open(img_path)
        width, height = cover.size
        
        width, height = float(width * 0.264583), float(height * 0.264583)
        
        pdf_size = {'P': (210, 297), 'L': (297, 210)}
        
        orientation = 'P' if width < height else 'L'
        
        width = width if width < pdf_size[orientation][0] else pdf_size[orientation][0]
        height = height if height < pdf_size[orientation][1] else pdf_size[orientation][1]
        
        pdf.add_page(orientation = orientation)
        pdf.image(img_path, 0, 0, width, height)

pdf_output = folder_name + ".pdf"
pdf.output(pdf_output, "F")

print(f"PDF file {pdf_output} created successfully.")
