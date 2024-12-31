from typing import Any

import cv2
import numpy as np
from cv2 import Mat
from numpy import ndarray, dtype

imageInputPath = 'images/Lena_rgb.bmp'
# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

cv2.imshow("Image", image)

image_cvtColor: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print(f"{image_cvtColor.shape = }")
print(f"{image_cvtColor.dtype = }")
print(f"{image_cvtColor = }")
cv2.imshow("Image Converted", image_cvtColor)

cv2.waitKey()
cv2.destroyAllWindows()