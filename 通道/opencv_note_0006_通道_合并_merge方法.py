import cv2
import numpy as np

# 分别读取 blue、green、red 三个通道
blueImageInputPath = '../images/Lena_rgb_blue.bmp'
greenImageInputPath = '../images/Lena_rgb_green.bmp'
redImageInputPath = '../images/Lena_rgb_red.bmp'

blueChannelImage: np.ndarray = cv2.imread(blueImageInputPath,
                                          flags=cv2.IMREAD_UNCHANGED)
greenChannelImage: np.ndarray = cv2.imread(greenImageInputPath,
                                           flags=cv2.IMREAD_UNCHANGED)
redChannelImage: np.ndarray = cv2.imread(redImageInputPath,
                                         flags=cv2.IMREAD_UNCHANGED)

if blueChannelImage is None:
    raise RuntimeError(f"Failed to load image at '{blueImageInputPath}'.")

if greenChannelImage is None:
    raise RuntimeError(f"Failed to load image at '{greenImageInputPath}'.")

if redChannelImage is None:
    raise RuntimeError(f"Failed to load image at '{redImageInputPath}'.")

# 分别绘制 blue、green、red 三个通道
cv2.imshow("Blue Channel", blueChannelImage)
print(f"{blueChannelImage.shape = }")
print(f"{blueChannelImage = }")

cv2.imshow("Green Channel", greenChannelImage)
print(f"{greenChannelImage.shape = }")
print(f"{greenChannelImage = }")

cv2.imshow("Red Channel", redChannelImage)
print(f"{redChannelImage.shape = }")
print(f"{redChannelImage = }")

# 使用 cv2.merge 方法合并 blue、green、red 三个通道
bgrImage: np.ndarray = cv2.merge([blueChannelImage,
                                  greenChannelImage,
                                  redChannelImage])
print(f"{bgrImage.shape = }")
print(f"{bgrImage = }")

cv2.imshow("BGR Image", bgrImage)

# 等待用户按键
cv2.waitKey()
cv2.destroyAllWindows()
