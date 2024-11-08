import cv2
import numpy as np

# 设置图像的宽和高
width, height = 512, 512

# 生成一个二值灰度图像，仅包含0和255
binary_image = np.zeros((height, width), dtype=np.uint8)

# 设置图像的每个像素值为0或255，形成棋盘格效果
for i in range(height):
    for j in range(width):
        if (i // 64 + j // 64) % 2 == 0:  # 每隔64像素切换0和255
            binary_image[i, j] = 0
        else:
            binary_image[i, j] = 255

# 显示图像
cv2.imshow("Binary Grayscale Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存图像
cv2.imwrite("images/watermarker.bmp", binary_image)
