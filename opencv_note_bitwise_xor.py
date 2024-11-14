import cv2
import numpy as np

# 定义图像输入路径
imageInputPath: str = 'images/Lena_gray.bmp'

# 读取图像文件
image: np.ndarray = cv2.imread(imageInputPath, flags=cv2.IMREAD_GRAYSCALE)

# 如果图像读取失败，则抛出运行时错误
if image is None:
    raise RuntimeError(f"Failed to load image.")

# 显示原始图像
cv2.imshow("Image", image)

# 生成与原始图像大小相同的马赛克图像
mosaic: np.ndarray = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)
# 显示生成的马赛克图像
cv2.imshow("Mosaic", mosaic)

# 创建一个与图像大小相同的脸部掩码
faceMask: np.ndarray = np.zeros_like(image, dtype=np.uint8)
# 在脸部区域设置掩码为255，即白色，也可以是任意非0值
faceMask[220:400, 250:360] = 1
cv2.imshow("Face Mask", faceMask)

# 创建图像的副本，并应用马赛克效果
image_with_mosaic: np.ndarray = image.copy()
# 使用位异或操作将马赛克应用于图像的特定区域（由掩码指定）
cv2.bitwise_xor(image, mosaic, dst=image_with_mosaic, mask=faceMask)
# 显示应用马赛克后的图像
cv2.imshow("Image with Mosaic", image_with_mosaic)

# 等待按键事件
cv2.waitKey()
# 关闭所有创建的窗口
cv2.destroyAllWindows()
