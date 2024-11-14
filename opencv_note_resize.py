import cv2
import numpy as np

imageInputPath = 'images/Lena_gray.bmp'

# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_GRAYSCALE)
print(f"{image.shape = }")

height, width = image.shape

imageResized1: np.ndarray[np.uint8] = cv2.resize(image, dsize=(width, height * 2))
print(f"{imageResized1.shape = }")

imageResized2: np.ndarray[np.uint8] = cv2.resize(image, dsize=None, fx=2, fy=1)
print(f"{imageResized2.shape = }")

# 显示图像
cv2.imshow("Image", image)
cv2.imshow("Image Resized 1", imageResized1)
cv2.imshow("Image Resized 2", imageResized2)

cv2.waitKey()
cv2.destroyAllWindows()
