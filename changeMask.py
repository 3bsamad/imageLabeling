
"""
Created on Fri Oct 25 17:53:30 2019
@author: Omar M. Abdel Samad
"""
#import the required packages
import cv2
import numpy as np
from PIL import Image

#the mask already created with only black and white 
mask= Image.open("label1.png")


img = mask.convert("RGBA")
pixdata = img.load()  
for y in range(img.size[1]):
    for x in range(img.size[0]):
        r, g, b, a = img.getpixel((x, y))
        if (r ==255) and (g ==255) and (b ==255):
            pixdata[x, y] = (150, 0, 0, 500) #red color of value 150 
        if r == 0 and g == 0 and b == 0:
            pixdata[x, y] = (0, 0, 0, 1000)
                       
img.save("redmask.png")






