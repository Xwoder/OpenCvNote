import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

image = cv2.imread("images/Lena_gray.bmp", flags=cv2.IMREAD_GRAYSCALE)

print(image.shape)
print(f"{image[0, 0] = :b}")

if image is None:
    raise RuntimeError("Failed to load image.")

bitPlanes = {}

for i in range(8):
    bitPlane: np.ndarray = (image & (1 << i)) >> i
    bitPlanes[i] = bitPlane

# 创建 1x4 的网格
fig: Figure
axs: np.ndarray[Axes]
fig, axs = plt.subplots(2, 4)
for index, bitPlane in bitPlanes.items():
    rowIndex: int = index // 4
    columnIndex: int = index % 4
    curAxes: Axes = axs[rowIndex, columnIndex]

    image = cv2.cvtColor(bitPlane * 0xFF, cv2.COLOR_BGR2RGB)
    curAxes.imshow(image)
    curAxes.axis('off')
    curAxes.set_title(f"Bit Plane {index}")
fig.tight_layout(pad=0.1)
plt.show()
