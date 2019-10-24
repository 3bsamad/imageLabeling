#a Python function to remove the green background. 
from PIL import Image  
from PIL import ImageFilter 
import numpy as np
import os
import cv2


#Creates a new image(numpy array) filled with certain color in RGB
def create_blank(width, height):
    # Create black blank image
    image = np.zeros((height, width, 1), np.uint8)
    # Fills image with color
    image[:] = 255 #whole array is 255
 
    return image



#defining a method to extract the green background, given an image as input
def removeBg(img):
    img = img.convert("RGBA")
    pixdata = img.load()  
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b, a = img.getpixel((x, y))
            if (r < 100) and (g >110) and (b < 170):
                pixdata[x, y] = (0, 0, 0, 1000) #black background
            if r == 0 and g == 0 and b == 0:
                pixdata[x, y] = (0, 0, 0, 1000)
    img2 = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    return img2


def removeBgHSV(img):
    #converts the image into HSV
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #splits the image in 3 channels: H, S, V
    h,s,v = cv2.split(img_hsv)
    
    cv2.imshow("H", h)
    cv2.imshow("s", s)
    cv2.imshow("v", v)
    
    #height, width, channel of each image
    h,w,c = img.shape
    
    mask = create_blank(w, h)
     
    for x in range(h):
        for y in range(w):
            s = img_hsv[x,y][1] #extracting only the s channel
            if s > 168:
                img[x,y] = (0,0,0)
                mask[x,y] = (0)
                
    #cv2.imshow("Mask", mask)
    #cv2.imshow("img", img)
    cv2.waitKey(1)
    
    return img, mask #returns a tuple containing both img and mask




#defining a method to apply threshold
def thresh_trunc(img):
    ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    return thresh



#going through images, removing the Background in each one
i=1
for filename in os.listdir("./input"): # parse through file list in the current directory
    if filename.endswith(".png"):
        img_original = cv2.imread("./input/" + filename)
        gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("Directory/output/original"+str(i)+".png",img_original)
        cv2.imwrite("Directory/output/gray"+str(i)+".png",gray)
        img, mask= removeBgHSV(img_original)
        cv2.imwrite("Directory/output/label"+str(i)+".png",mask)
        cv2.imwrite("Directory/output/img"+str(i)+".png",img)
        
        i+=1
    i+=1
   

j=1 
for filename in os.listdir("."): # parse through file list in the current directory
    if filename.endswith(".png"):
        print(filename)
        img =cv2.imread(filename)
        img=thresh_trunc(img)
        #adding text to each image
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (550,430)
        fontScale              = 1
        fontColor              = (255,255,255)
        lineType               = 2
        cv2.putText(img,'Hand', bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
        j+=1    
    j+=1
    cv2.imwrite("Directory/photo"+str(j)+".png",img) 



       
    
        
                   
            
            
             
    












