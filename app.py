import cv2
import numpy as np 

from project import *

filename="images\input\image1.jpg"

cartoonizer(filename,3,10,7,7)

img=cv2.imread(filename)
img2=cv2.imread("images\output\Cartoon.png")

cv2.imshow("Original Image",img)
cv2.imshow("Cartoonized Image",img2)

cartoonizer(filename,3,100,7,7)

img=cv2.imread(filename)
img2=cv2.imread("images\output\Cartoon.png")

cv2.imshow("Original Image1",img)
cv2.imshow("Cartoonized Image1",img2)

cartoonizer(filename,3,256,3,15)

img=cv2.imread(filename)
img2=cv2.imread("images\output\Cartoon.png")

cv2.imshow("Original Image2",img)
cv2.imshow("Cartoonized Image2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()