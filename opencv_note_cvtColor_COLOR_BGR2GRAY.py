from typing import Any

import cv2
import numpy as np
from cv2 import Mat
from numpy import ndarray, dtype

imageInputPath = 'images/Lena_rgb.bmp'
# 读出图像从文件
image: np.ndarray = cv2.imread(imageInputPath,
                               flags=cv2.IMREAD_UNCHANGED)

cv2.imshow("Image", image)

# ### 代码解释
#
# 这段代码的功能是将输入的图像从BGR颜色空间转换为灰度图像。具体步骤如下：
#
# 1. 使用 `cv2.cvtColor` 函数进行颜色空间转换。
# 2. 输入参数为原图像 `image` 和颜色转换码 `cv2.COLOR_BGR2GRAY`。
# 3. 输出结果为灰度图像 `image_converted`。
#
# ### 控制流图
#
# 由于这段代码逻辑简单，直接用一个节点表示即可。
#
# ```mermaid
# flowchart TD
#     A[开始] -->|调用 cvtColor 函数| B[转换为灰度图像]
# ```
#
# 此图展示了从原始图像到灰度图像的转换过程。
image_cvtColor: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(f"{image_cvtColor.shape = }")
print(f"{image_cvtColor.dtype = }")
print(f"{image_cvtColor = }")
cv2.imshow("Image Converted", image_cvtColor)

cv2.waitKey()
cv2.destroyAllWindows()