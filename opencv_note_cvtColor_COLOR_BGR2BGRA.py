import cv2
import numpy as np

imageInputPath = 'images/Lena_rgb.bmp'
# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

cv2.imshow("Image", image)

image_cvtColor: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
print(f"image_cvtColor.shape: {image_cvtColor.shape}")
print(f"image_cvtColor.dtype: {image_cvtColor.dtype}")
print(f"image_cvtColor: {image_cvtColor}")

b, g, r, a = cv2.split(image_cvtColor)
a[:, :] = 100

image_cvtColor = cv2.merge((b, g, r, a))

cv2.imshow("Image Converted", image_cvtColor)
cv2.imwrite("images/Lena_rgb_bgra.png", image_cvtColor)

cv2.waitKey()
cv2.destroyAllWindows()
