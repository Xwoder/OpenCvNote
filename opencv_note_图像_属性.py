import cv2
import numpy as np

imageInputPath = 'images/Lena_gray.bmp'

# 读取图像文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_GRAYSCALE)

if image is None:
    raise RuntimeError(f"Failed to load image.")

print(f"{image = }")
print(f"{image.shape = }")
print(f"{image.size = }")
print(f"{image.dtype = }")

cv2.imshow("Image", image)

cv2.waitKey()

cv2.destroyAllWindows()
