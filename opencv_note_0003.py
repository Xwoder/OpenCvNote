import cv2
import numpy as np

imageInputPath = 'images/Lena_rgb.bmp'
imageOutputPath = 'images/LenaRGB_copy.bmp'

# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

print(f"{image.shape = }")
print(f"{image[0][0] = }")
print(f"{image = }")

# 窗口名称
windowName: str = "Image"

# 创建指定名称的窗口
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow(windowName, image)

# 等待用户按键
cv2.waitKey()

# 写入图像至文件
cv2.imwrite(imageOutputPath, image)

# 销毁全部窗口
cv2.destroyAllWindows()
