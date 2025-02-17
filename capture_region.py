import cv2

def select_region(image):
    clone = image.copy()
    roi = {"x": 0, "y": 0, "w": 0, "h": 0}
    drawing = False
    ix, iy = -1, -1

    def mouse_callback(event, x, y, flags, param):
        nonlocal ix, iy, drawing, roi, clone
        temp = clone.copy()
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                cv2.rectangle(temp, (ix, iy), (x, y), (0, 255, 0), 2)
                cv2.imshow("Select ROI", temp)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            roi["x"] = min(ix, x)
            roi["y"] = min(iy, y)
            roi["w"] = abs(x - ix)
            roi["h"] = abs(y - iy)
            cv2.rectangle(temp, (roi["x"], roi["y"]), (roi["x"] + roi["w"], roi["y"] + roi["h"]), (0, 255, 0), 2)
            cv2.imshow("Select ROI", temp)

    cv2.namedWindow("Select ROI")
    cv2.setMouseCallback("Select ROI", mouse_callback)

    # ユーザーが Enter キーを押すまで待機（ROIの確認）
    while True:
        cv2.imshow("Select ROI", clone)
        key = cv2.waitKey(1) & 0xFF
        if key == 13:  # Enter キーで確定
            break

    cv2.destroyWindow("Select ROI")
    return roi["x"], roi["y"], roi["w"], roi["h"]
