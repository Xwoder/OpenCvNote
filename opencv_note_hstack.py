import cv2
import numpy as np

# 定义图片的尺寸
height, width = 200, 200

# 创建红色、绿色、蓝色图片
red_image = np.zeros((height, width, 3), dtype=np.uint8)
red_image[:, :] = (0, 0, 255)  # BGR 格式，红色

green_image = np.zeros((height, width, 3), dtype=np.uint8)
green_image[:, :] = (0, 255, 0)  # BGR 格式，绿色

blue_image = np.zeros((height, width, 3), dtype=np.uint8)
blue_image[:, :] = (255, 0, 0)  # BGR 格式，蓝色

stacked_image = np.hstack((red_image, green_image, blue_image))

# 显示图片
cv2.imshow("Red Image", red_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Blue Image", blue_image)
cv2.imshow("Stacked Image", stacked_image)

# 等待用户按键后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
