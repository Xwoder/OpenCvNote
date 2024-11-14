import cv2
import numpy as np

"""
演示 OpenCV 中，常用的方法：
- imread
- imwrite
- namedWindow
- imshow
- waitKey
- destroyAllWindows
"""

imageInputPath = 'images/Lena_gray.bmp'
imageOutputPath = 'images/Lena_gray_copy.bmp'

# 读取图像文件
image: np.ndarray = cv2.imread(imageInputPath, flags=cv2.IMREAD_GRAYSCALE)
if image is None:
    raise RuntimeError(f"Failed to load image.")

print(f"{image.shape = }")
print(f"{image = }")

# 窗口名称
windowName: str = "Image"

# 创建指定名称的窗口，可选操作
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# 在指定的窗口名称中显示图像
# 如果没有通过 cv2.namedWindow() 创建指定名称窗口，则该方法会根据给定的名称创建一个默认的窗口
cv2.imshow(windowName, image)

# waitKey方法，用于接收键盘按键，返回按键的 ASCII 码
# 如果 delay 为 0，则表示该方法会一直等待，直到接收到按键，否则该方法会等待指定的时间，超时则返回 -1
keyCode: int = cv2.waitKey(delay=5000)
print(f"{keyCode = }")

# 写入图像至文件
cv2.imwrite(imageOutputPath, image)

# destroyAllWindows方法，其接受一个可选的窗口名称，用于销毁指定窗口，否则销毁全部窗口
cv2.destroyAllWindows()
