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

car_list.append(Car("Williams", "AA", "#4e6cd9", (847, 126)))


for car in car_list:
    patch = pat.Circle(car.pos, 20, color = car.colour)
    ax.add_patch(patch)
    ax.annotate(car.driver, car.pos, color = "black")

#updating position

for i in range(curve_points):
    car.pos = curve_points[i]
    ax.clear()
    time.sleep(0.5)


plt.show()