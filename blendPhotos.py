# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:55:45 2019

@author: Omar M. Abdel Samad
"""

from __future__ import print_function
import cv2 as cv
alpha = 0.5
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')
input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
    alpha = input_alpha
# [load]
src2 = cv.imread("gray1.png")
src1 = cv.imread("redmask.png")
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
beta = 1.0
dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()

cv.imwrite("labelledImage.png",dst)
