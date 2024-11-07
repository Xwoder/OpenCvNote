import cv2
import numpy as np

imageWidth: int = 3
imageHeight: int = 4

image1: np.ndarray = np.random.randint(0, 256,
                                       size=(imageWidth, imageHeight),
                                       dtype=np.uint8)
image2: np.ndarray = np.random.randint(0, 256,
                                       size=(imageWidth, imageHeight),
                                       dtype=np.uint8)

print(f"{image1 = }")
print(f"{image2 = }")

# 计算公式：
# cv2.add = np.min(image1 + image2, 255)
imagePlus: np.ndarray = cv2.add(image1, image2)

print(f"{imagePlus = }")

for i in range(imageWidth):
    for j in range(imageHeight):
        print(f"{image1[i, j]:>3d}+{image2[i, j]:<3d}={imagePlus[i, j]:<3d}", end=", ")
    print()
