#simulation file for car project

import cv2
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.image as im
from class_file import Car
import time

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

car_list.append(Car("McLaren", "LN", "#c84274", (213, 326)))
car_list.append(Car("Williams", "AA", "#4e6cd9", (847, 126)))
car_list.append(Car("Ferrari", "CL", "#c92216", (213, 326)))




for i in range(0, len(curve_points)):
    ax.clear()
    ax.imshow(track)


    for j, car in enumerate(car_list):
    
        index = (i*(j+25)) % len(curve_points)
        car.pos = curve_points[index]
        patch = pat.Circle(car.pos, 20, color = car.colour)
        ax.add_patch(patch)
        ax.annotate(car.driver, car.pos, color = "black")
    
    fig.canvas.draw_idle()
    plt.pause(0.1)


plt.close(fig) 


