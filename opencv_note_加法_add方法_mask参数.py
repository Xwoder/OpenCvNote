import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# 创建两个示例图像
img_green = np.full((300, 300, 3), (0, 255, 0), dtype=np.uint8)  # 绿色图像
img_red = np.full((300, 300, 3), (0, 0, 255), dtype=np.uint8)  # 红色图像

# 创建掩码：部分为0，部分为128，部分为255
mask = np.zeros((300, 300), dtype=np.uint8)
cv2.rectangle(mask, (50, 50), (150, 150), 255, -1)  # 白色区域(255)
cv2.rectangle(mask, (150, 150), (250, 250), 128, -1)  # 灰色区域(128)

# 使用掩码进行加法
result = cv2.add(img_green, img_red, mask=mask)

# 显示
fig: Figure
axs: np.ndarray[Axes]
fig, axs = plt.subplots(2, 2)

axs[0, 0].imshow(cv2.cvtColor(img_green, cv2.COLOR_BGR2RGB))
axs[0, 0].axis('off')
axs[0, 0].set_title('Image Green')

axs[0, 1].imshow(cv2.cvtColor(img_red, cv2.COLOR_BGR2RGB))
axs[0, 1].axis('off')
axs[0, 1].set_title('Image Red')

axs[1, 0].imshow(mask, cmap='gray')
axs[1, 0].axis('off')
axs[1, 0].set_title('Mask')

axs[1, 1].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
axs[1, 1].axis('off')
axs[1, 1].set_title('Masked Add Result')

fig.tight_layout(pad=0.1)
plt.show()
