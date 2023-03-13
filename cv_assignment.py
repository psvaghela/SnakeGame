# Roll Number: U20ME086
# Name: Parthivsinh Vaghela

import cv2
import math
import numpy

img = cv2.imread('cva1.jpeg')
height = img.shape[0]
width = img.shape[1]

centerx = width//2
centery = height//2

rotated = numpy.copy(img)

# For rotation of image by angle θ
# x_new = xsin(θ) - ysin(θ)
# y_new = xsin(θ) + ysin(θ)

# Angle of rotation = 70 degrees
angle = math.radians(70)
for i in range(height):
    for j in range(width):
        x= (i-centerx)*math.cos(angle)+(j-centery)*math.sin(angle)
        y= -(i-centerx)*math.sin(angle)+(j-centery)*math.cos(angle)

        x=round(x)+centerx 
        y=round(y)+centery 

        if (x>=0 and y>=0 and x<height and  y<width):
            rotated[i,j] = img[x,y]
        else:
            rotated[i,j] = img[0,0]

# Saving image
cv2.imwrite("rotated.jpeg", rotated)