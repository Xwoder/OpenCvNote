import cv2
import numpy as np

imageInputPath = 'images/Lena_rgb.bmp'
# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

cv2.imshow("Image", image)

image2: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(image2)
h[:, :] = h[:, :] + 10
s[:, :] = s[:, :] + 20
image2 = cv2.merge([h, s, v])

image2 = cv2.cvtColor(image2, cv2.COLOR_HSV2BGR)

cv2.imshow("Image Converted", image2)

cv2.waitKey()
cv2.destroyAllWindows()
