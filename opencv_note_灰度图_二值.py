import cv2
import numpy as np

# OpenCV 中的二值图像，0表示黑色，255表示白色
# 可以理解成特殊的灰度图像

blockWindowName: str = "Black"
blackImage: np.ndarray = np.zeros((512, 512), dtype=np.uint8)

print(f"{blackImage = }")
print(f"{blackImage[0, 0] = }")
cv2.namedWindow(blockWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(blockWindowName, blackImage)

whiteWindowName: str = "White"
whiteImage: np.ndarray = np.full((512, 512), fill_value=255, dtype=np.uint8)
print(f"{whiteImage = }")
print(f"{whiteImage[0, 0] = }")
cv2.namedWindow(whiteWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(whiteWindowName, whiteImage)

# 等待用户按键
cv2.waitKey()

# 销毁全部窗口
cv2.destroyAllWindows()