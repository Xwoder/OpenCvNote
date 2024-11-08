import cv2
import numpy as np

imageInputPath = 'images/Lena_gray.bmp'

watermarkInputPath = 'images/watermark.bmp'

def watermark_embed(image: np.ndarray[np.uint8],
                    watermark: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """
    将水印嵌入到图像中。

    将输入的水印转换为二值形式，并将其嵌入到图像中。该函数使用位操作来实现水印的嵌入，
    确保水印在嵌入后对原始图像的影响尽可能小。

    参数:
    image: 输入的图像，类型为np.ndarray[np.uint8]。
    watermark: 输入的水印，类型为np.ndarray[np.uint8]。

    返回:
    返回嵌入水印后的图像，类型为np.ndarray[np.uint8]。
    """
    # 将水印转换为二值形式，这里使用阈值处理来确保水印的每个像素仅为0或1
    watermark_binary: np.ndarray[np.uint8]
    _, watermark_binary = cv2.threshold(watermark, thresh=127, maxval=1, type=cv2.THRESH_BINARY)
    # 显示二值化后的水印，这里乘以255是为了在显示时恢复为原始的黑白效果
    cv2.imshow("Watermark Binary", watermark_binary * 255)

    # 创建一个与输入图像大小相同，但所有像素值为0xFE的矩阵
    # 这是为了在嵌入水印时，保留原始图像的最高位，从而减少对图像质量的影响
    matrix = np.full_like(image, fill_value=0xFF - 1, dtype=np.uint8)

    # 使用位操作来嵌入水印
    # 首先使用cv2.bitwise_and函数将图像与matrix_embed进行按位与操作，然后使用cv2.bitwise_or函数将结果与水印进行按位或操作
    # 这样可以在不显著改变原始图像的同时，将水印信息嵌入到图像中
    imaged_watermark_embedded = cv2.bitwise_or(
        cv2.bitwise_and(image, matrix),
        watermark_binary)

    # 返回嵌入水印后的图像
    return imaged_watermark_embedded


def watermark_extract(image: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """
    从给定图像中提取水印。

    该函数的目的是从输入的图像中提取出隐藏的水印。它首先创建一个与输入图像形状相同的矩阵，
    然后使用OpenCV的位运算和阈值处理功能来提取水印。

    参数:
    image (np.ndarray[np.uint8]): 输入的包含水印的图像。

    返回:
    np.ndarray[np.uint8]: 提取出来的水印图像。
    """
    # 创建一个与输入图像形状相同，但所有元素值为1的矩阵
    matrix = np.full_like(image, fill_value=1, dtype=np.uint8)

    # 使用位与操作来提取图像中的水印信息
    watermark_binary = cv2.bitwise_and(image_watermark_embedded, matrix)

    # 使用阈值处理来二值化提取的水印信息，以便清晰地显示水印
    _, watermark = cv2.threshold(watermark_binary, thresh=0, maxval=0xFF, type=cv2.THRESH_BINARY)

    # 返回提取并处理后的水印图像
    return watermark
# 读取图像文件
image: np.ndarray[np.uint8] = cv2.imread(imageInputPath, flags=cv2.IMREAD_GRAYSCALE)

watermark: np.ndarray[np.uint8] = cv2.imread(watermarkInputPath, flags=cv2.IMREAD_GRAYSCALE)

if image is None or watermark is None:
    raise RuntimeError(f"Failed to load image.")
cv2.imshow("Image", image)


cv2.imshow("Watermark", watermark)


image_watermark_embedded: np.ndarray[np.uint8] = watermark_embed(image, watermark)
cv2.imshow("Image Embedded In Watermark", image_watermark_embedded)

watermark_extract: np.ndarray[np.uint8] = watermark_extract(image_watermark_embedded)
cv2.imshow("Watermark Extract", watermark_extract)

cv2.waitKey()
cv2.destroyAllWindows()
