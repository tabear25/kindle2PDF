print('座標を計測します')

import win32gui
import time

# 7秒の間に、kindleの画面に移動して待機
time.sleep(7)

def get_window_rect():
    # アクティブなウィンドウのハンドルを取得
    hwnd = win32gui.GetForegroundWindow()
    
    # ウィンドウの座標を取得
    rect = win32gui.GetWindowRect(hwnd)
    
    left, top, right, bottom = rect
    width = right - left
    height = bottom - top
    
    return left, top, width, height

if __name__ == "__main__":
    left, top, width, height = get_window_rect()
    print(f"Left: {left}, Top: {top}, Width: {width}, Height: {height}")
