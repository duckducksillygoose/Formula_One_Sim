#simulation file for car project

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.image as im
from class_file import Car

#getting contours from image
image = cv2.imread('barcelona.png', cv2.IMREAD_GRAYSCALE)
image = cv2.bitwise_not(image)
ret, binary_image = cv2.threshold(image, 127, 255, 0)
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

curve_points = contours[0].reshape(-1, 2)

print(curve_points)

fig,ax = plt.subplots()
ax.set_xlim(0, 1200)
ax.set_ylim(0,800)

ax.invert_yaxis()

track= im.imread('barcelona.png')
plt.imshow(track)

car_list = []
for car in car_list:
    plot_me(car)

plt.show()