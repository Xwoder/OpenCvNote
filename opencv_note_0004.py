import cv2
import numpy as np

# 读出图像从文件
image: np.ndarray = np.zeros(shape=(600, 600, 3), dtype=np.uint8)

# 前三分之一列填充红色
image[:, :200] = (0, 0, 255)  # 红色
# 中三分之一列填充绿色
image[:, 200:400] = (0, 255, 0)  # 绿色
# 后三分之一列填充蓝色
image[:, 400:] = (255, 0, 0)  # 蓝色

print(f"{image.shape = }")
print(f"{image = }")

# 访问
print(f"{image[0, 0] = }")
print(f"{image[0, 200] = }")
print(f"{image[0, 400] = }")

# 修改
image[288:302, 288:302, 0] = 255
image[288:302, 288:302, 1] = 255
image[288:302, 288:302, 2] = 255

# 窗口名称
windowName: str = "BGR Image"

# 创建指定名称的窗口
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow(windowName, image)

# 等待用户按键
cv2.waitKey()

# 销毁全部窗口
cv2.destroyAllWindows()
