from PIL import Image, ImageDraw, ImageFilter
import cv2
import numpy as np 
import random
import os
import imageio
import imgaug as ia
import imgaug.augmenters as iaa
# >>> converts an image from PIL format to be of cv2 format <<<
def pil2cv(pil_image):
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
# >>> converts an image from cv2 format to be of PIL format <<<
def cv2pil(cv_img):
    cv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(cv_img)
    return pil_img



###### >>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<< #######
path1 = "D:/CTJ-OE/hands/output-all/Originals/"
path2 = "D:/CTJ-OE/hands/output-all/Binary Masks/"

lab=Image.open("lab.jpg")
hands=[] #is a list containing hand files, which are of PIL format
masks=[] # Binary Masks of PIL format
i=0
for filename in os.listdir(path1): 
    if filename.endswith(".png") :
        print("processing hand files..")
        hand = Image.open(path1 + filename).resize((1600,1200)).rotate(270, expand = 1)
 
        hands.append(hand) 
        i+=1
print("hand files processing done!")
j=0
for filename in os.listdir(path2):
    if filename.endswith(".png") :
        print("processing mask files..")
        mask = Image.open(path2 + filename).resize((1600,1200)).rotate(270, expand = 1)
        masks.append(mask) 
        j+=1
print("mask files processing done!")

handsCV=[]
""" 
while j<len(hands):
    handCV = pil2cv(hands[j])
    ret, mask = cv2.threshold(handCV[:,:,0], 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    maskPIL=cv2pil(mask).resize((1600, 1200)).convert("RGBA")
    masks.append(maskPIL)
    j+=1
"""

lab_w, lab_h = lab.size
hand_w, hand_h = hands[0].size
c=0
while c<len(hands):
    print("merging file number "+ str(c+1))
    labCopy=lab.copy()
    labCopy.paste(hands[c],((random.randint(hand_w,(lab_w-hand_w)+1)),
    (lab_h-hand_h)),masks[c])
    labCopy.save("./merging/mrg-"+str(c)+".png")
    c+=1
    




