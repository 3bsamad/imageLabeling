# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:40:33 2019

@author: ctj-oe
"""

import cv2
import numpy as np
from PIL import Image
src1 = cv2.imread("img1.png")
src2 = cv2.imread("red.png")
mask= Image.open("label1.png")




img = mask.convert("RGBA")
pixdata = img.load()  
for y in range(img.size[1]):
    for x in range(img.size[0]):
        r, g, b, a = img.getpixel((x, y))
        if (r ==255) and (g ==255) and (b ==255):
            pixdata[x, y] = (150, 0, 0, 500) #black background
        if r == 0 and g == 0 and b == 0:
            pixdata[x, y] = (0, 0, 0, 1000)
            
            
img.save("redmask.png")






