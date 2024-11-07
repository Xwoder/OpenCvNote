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

# 加权和 = np.min(image * alpha + image2 * beta + gamma, 255)
imagePlus: np.ndarray = cv2.addWeighted(image1, 2,
                                        image2, 1,
                                        10)

print(f"{imagePlus = }")
