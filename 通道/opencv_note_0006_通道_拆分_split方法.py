import cv2
import numpy as np

# 读出图像从文件
imageInputPath = '../images/Lena_rgb.bmp'

# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

if image is None:
    raise RuntimeError(f"Failed to load image at '{imageInputPath}'.")

print(f"{image.shape = }")
print(f"{image = }")

blueChannel: np.ndarray
greenChannel: np.ndarray
redChannel: np.ndarray
blueChannel, greenChannel, redChannel = cv2.split(image)

print(f"{blueChannel.shape = }, {blueChannel = }")
print(f"{greenChannel.shape = }, {greenChannel = }")
print(f"{redChannel.shape = }, {redChannel = }")

# 窗口名称
rgbWindowName: str = "BGR Image"
cv2.namedWindow(rgbWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(rgbWindowName, image)

blueWindowName: str = "Blue Channel"
cv2.namedWindow(blueWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(blueWindowName, blueChannel)
cv2.imwrite("../images/Lena_rgb_blue.bmp", blueChannel)

greenWindowName: str = "Green Channel"
cv2.namedWindow(greenWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(greenWindowName, greenChannel)
cv2.imwrite("../images/Lena_rgb_green.bmp", greenChannel)

redWindowName: str = "Red Channel"
cv2.namedWindow(redWindowName, cv2.WINDOW_NORMAL)
cv2.imshow(redWindowName, redChannel)
cv2.imwrite("../images/Lena_rgb_red.bmp", redChannel)

# 等待用户按键
cv2.waitKey()
cv2.destroyAllWindows()
