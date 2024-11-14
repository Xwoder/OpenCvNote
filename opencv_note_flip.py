import cv2
import numpy as np

imageInputPath = 'images/Lena_gray.bmp'

# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_GRAYSCALE)

image1 = cv2.flip(image, flipCode=0)
image2 = cv2.flip(image, flipCode=1)
image3 = cv2.flip(image, flipCode=-1)

cv2.imshow("image", image)
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("image3", image3)

cv2.waitKey()
cv2.destroyAllWindows()
