import pyautogui
import time

print("座標を計測したい場所へマウスを動かしてください。ターミナルにカーソルを合わせてCtrl+Cで終了します。")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x} Y: {y}"
        print(position_str, end="")
        print("\b" * len(position_str), end="", flush=True)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nDone.")