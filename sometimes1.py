# applies image augmentation to the input pictures, only this time using sometimes, which means not every picture gets every augmentation process
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import cv2
import imageio
import os

#>>> First, going through the directory and
#>>> adding input images to the list images[]
images=[] #empty list
i=0
print("parsing file list and scanning for images..."+"\n")
for filename in os.listdir("D:/CTJ-OE/Augmentation/merging/"): # parse through file list 
    if filename.endswith(".png"):
        mask = imageio.imread("D:/CTJ-OE/Augmentation/merging/" + filename)
        images.append(mask) #add each file to the list  images[]
        i+=1

print("all input images added to list..\n")
print("number of input images is "+ str(len(images)) +"\n")
print("augmenting images...\n")



sometimes = lambda aug: iaa.Sometimes(0.6, aug)
sometimes2 = lambda aug: iaa.Sometimes(0.35, aug)

#>>> Sequence of augmenations applied to each image
seq_Augmentation = iaa.Sequential([
sometimes(iaa.MotionBlur(k=60, angle=[-180, 180])),
sometimes(iaa.GammaContrast((0.5, 1.5))),
sometimes(iaa.OneOf([
    iaa.AdditiveGaussianNoise(scale=0.1*255),
    iaa.AdditiveGaussianNoise(scale=0.1*255, per_channel=True),
    iaa.CloudLayer(210,-1.1,5,0.05,0.4,2000,-2.6,1.0,1.0)
    ])),
sometimes(iaa.OneOf([
        iaa.Fliplr(1.0),
        iaa.Flipud(1.0)
        ])),
sometimes2(iaa.AddToHueAndSaturation((-15, 15), per_channel=True)),
sometimes(iaa.Rot90((1), keep_size=True))
],
random_order=False)

Augmentation=seq_Augmentation.augment_images(images)



#>>> going through the list of Augmented images
#>>> and saving each image 
c=0
z=8351
while c<len(images):
    print("processing image #"+str(c)+"...")
    cv2.imwrite("./merge aug/mergeAug"+str(z)+".png",
                cv2.cvtColor(Augmentation[c],cv2.COLOR_BGR2RGB))
    c+=1
    z+=1
print("number of output images is "+ str(c))
    
    
    
    
    
    
