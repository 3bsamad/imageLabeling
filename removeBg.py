# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:50:27 2019

@author: Omar Elshenoudy
"""

#a Python function to remove the green background. 
from PIL import Image  
from PIL import ImageFilter 
import os

#defining a method to extract the green background, given an image as input
def removeBg(img):         
    img = img.convert("RGBA")  #red, green, blue, alpha for transparency- 0 absolute transparent
    pixdata = img.load()  
    for y in range(img.size[1]):  
        for x in range(img.size[0]):  
            r, g, b, a = img.getpixel((x, y)
            # the RGB values of the background                   
            if (r < 100) and (g >110) and (b < 170):
                # R,G,B, alpha for transparency                      
                pixdata[x, y] = (0, 0, 0, 1000)  
            #Removes anti-aliasing outline of body  
            if r == 0 and g == 0 and b == 0:  
                pixdata[x, y] = (0, 0, 0, 1000)
    # apply gaussian blur to smooth out the edges                                  
    img2 = img.filter(ImageFilter.GaussianBlur(radius=0.5))  
    return img2

 



      
