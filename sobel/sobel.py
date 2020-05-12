import sys
import matplotlib
import numpy as np
import cv2


#Create x - direction & y - direction kernels 

xkernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
ykernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

# Read in file from directory

img = cv2.imread('liberty.jpg')
cv2.imread('liberty.jpg')


#display original image


#cv2.imshow('liberty', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Store pixels into array

#Convert RGB pixels to greyscale

#Convolve in x - direction, store pixels in an array

#Convolve in y - direction, store pixels in an array

#Add both matrices together to produce the final image

