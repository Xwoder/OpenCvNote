# 导入必要的库
import cv2
import numpy as np

# 定义图像输入路径
imageInputPath: str = 'images/Lena_gray.bmp'

# 读取图像，以灰度模式
image: np.ndarray = cv2.imread(imageInputPath, flags=cv2.IMREAD_GRAYSCALE)

# 检查图像是否成功加载
if image is None:
    raise RuntimeError(f"Failed to load image.")

# 显示原始图像
cv2.imshow("Image", image)

# 生成一个随机的密钥图像，尺寸和原始图像相同
key: np.ndarray = np.random.randint(0, 256,
                                    size=image.shape,
                                    dtype=np.uint8)
# 显示密钥图像
cv2.imshow("Key", key)

# 使用位运算异或对图像进行加密
imageEncrypted: np.ndarray = cv2.bitwise_xor(image, key)
# 显示加密后的图像
cv2.imshow("Encrypted Image", imageEncrypted)

# 再次使用位运算异或对加密图像进行解密
imageDecrypted: np.ndarray = cv2.bitwise_xor(imageEncrypted, key)
# 显示解密后的图像
cv2.imshow("Decrypted Image", imageDecrypted)

# 等待按键事件
cv2.waitKey()
# 关闭所有显示窗口
cv2.destroyAllWindows()
