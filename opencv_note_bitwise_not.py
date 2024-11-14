import cv2
import numpy as np

imageInputPath = 'images/Lena_gray.bmp'

# 读取图像文件
image: np.ndarray = cv2.imread(imageInputPath, flags=cv2.IMREAD_GRAYSCALE)

if image is None:
    raise RuntimeError(f"Failed to load image.")

cv2.imshow("Image", image)

# 面部掩码
faceMask: np.ndarray = np.zeros_like(image, dtype=np.uint8)
faceMask[220:400, 250:360] = 1

# 复制原始图片
imageColorInverted: np.ndarray = np.copy(image)

# 对输入的图像进行按位取反操作，实现颜色反转
# 参数image: 原始图像
# 参数dst: 目标图像，存储颜色反转后的结果
# 参数mask: 处理遮罩，只有在遮罩非黑色的部分才会进行颜色反转
cv2.bitwise_not(image, dst=imageColorInverted, mask=faceMask)

# 显示颜色反转后的图像
cv2.imshow("Image with Invert Color", imageColorInverted)

cv2.waitKey()
cv2.destroyAllWindows()
