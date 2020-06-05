## applies a number of image augmentation processes to the pictures
import imageio
import imgaug as ia
from imgaug.augmentables.polys import Polygon, PolygonsOnImage
import numpy as np
import cv2
from imgaug import augmenters as iaa
import os

images=[] #empty list
i=0
for filename in os.listdir("./inputs/"): # parse through file list 
    if filename.endswith(".png"):
        mask = imageio.imread("./inputs/" + filename)
        images.append(mask) #add each file to the list images[]
        i+=1


print("number of input images is "+ str(len(images)) +"\n")


"""^^^ Augmentation sequences to be applied to each image ^^^

seq_AdditiveGaussianNoise: applies Additive Gaussian Noise
seq_AGN_per_channel: applies Additive Gaussian Noise per channel
seq_AdditiveLaplaceNoise: applies Additive Laplacian Noise
seq_ALN_per_channel: applies Additive Laplacian Noise per channel
seq_Rot90 : rotates by 90°
seq_GammaContrast: applies Gamma Contrast
seq_GammaContrast_per_channel: applies Gamma Contrast per channel 
seq_Fliplr: flips images horizontally
seq_Flipud: flips images vertically
seq_AddToHueAndSaturation: Adds random values between -50 and 50 to hue and saturation
seq_Multiply: multiplies each image with a random value between 0.5 and 1.5 
"""
seq_AdditiveGaussianNoise = iaa.Sequential([iaa.AdditiveGaussianNoise(scale=0.1*255)])
seq_AGN_per_channel=iaa.Sequential([iaa.AdditiveGaussianNoise(scale=0.1*255, per_channel=True)])
seq_AdditiveLaplaceNoise=iaa.Sequential([iaa.AdditiveLaplaceNoise(scale=0.1*255)])
seq_ALN_per_channel=iaa.Sequential([iaa.AdditiveLaplaceNoise(scale=0.1*255,per_channel=True)])  
seq_Rot90 = iaa.Sequential([iaa.Rot90(1)])
seq_GammaContrast = iaa.Sequential([iaa.GammaContrast((0.5, 1.5))])
seq_GammaContrast_per_channel= iaa.Sequential([iaa.GammaContrast((0.5, 1.5), per_channel=True)])
seq_MotionBlur=iaa.Sequential([iaa.MotionBlur(k=15, angle=[-180, 180])])
seq_Fliplr=iaa.Sequential([iaa.Fliplr(1.0)])
seq_Flipud=iaa.Sequential([iaa.Flipud(1.0)])
seq_AddToHueAndSaturation=iaa.Sequential([iaa.AddToHueAndSaturation((-50, 50), per_channel=True)])
seq_Multiply=iaa.Sequential([iaa.Multiply((0.5, 1.5))]) 
seq_Clouds=iaa.Sequential([iaa.Clouds()])

#lists containing the augmented images, named like each corresponding sequence from above
AdditiveGaussianNoise=seq_AdditiveGaussianNoise.augment_images(images)
AGN_per_channel=seq_AGN_per_channel.augment_images(images)
AdditiveLaplaceNoise=seq_AdditiveLaplaceNoise.augment_images(images)
ALN_per_channel=seq_ALN_per_channel.augment_images(images)
Rot90=seq_Rot90.augment_images(images)
GammaContrast = seq_GammaContrast.augment_images(images)
GammaContrast_per_channel=seq_GammaContrast_per_channel.augment_images(images)
MotionBlur=seq_MotionBlur.augment_images(images)
Fliplr=seq_Fliplr.augment_images(images)
Flipud=seq_Flipud.augment_images(images)
AddToHueAndSaturation=seq_AddToHueAndSaturation.augment_images(images)
Multiply=seq_Multiply.augment_images(images)
Clouds=seq_Clouds.augment_images(images)




#now the original list (images[]) contains the input images 
#each list from above contains the corresponding augmented images
c=0
for img in images:
    print(c)
    cv2.imwrite("./augmentation test/AdditiveGaussianNoise"+str(c)+".png",
                cv2.cvtColor(AdditiveGaussianNoise[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/AGN_per_channel"+str(c)+".png",
                cv2.cvtColor(AGN_per_channel[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/AdditiveLaplaceNoise"+str(c)+".png",
                cv2.cvtColor(AdditiveLaplaceNoise[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/ALN_per_channel"+str(c)+".png",
                cv2.cvtColor(ALN_per_channel[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/Rot90"+str(c)+".png",
                cv2.cvtColor(Rot90[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/GammaContrast"+str(c)+".png",
                cv2.cvtColor(GammaContrast[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/GammaContrast_per_channel"+str(c)+".png",
                cv2.cvtColor(GammaContrast_per_channel[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/MotionBlur"+str(c)+".png",
                cv2.cvtColor(MotionBlur[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/Fliplr"+str(c)+".png",
                cv2.cvtColor(Fliplr[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/Flipud"+str(c)+".png",
                cv2.cvtColor(Flipud[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/AddToHueAndSaturation"+str(c)+".png",
                cv2.cvtColor(AddToHueAndSaturation[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/Multiply"+str(c)+".png",
                cv2.cvtColor(Multiply[c],cv2.COLOR_BGR2RGB))
    cv2.imwrite("./augmentation test/Clouds"+str(c)+".png",
                cv2.cvtColor(Clouds[c],cv2.COLOR_BGR2RGB))
    c+=1






#aug = iaa.AdditiveGaussianNoise(scale=0.1*255)

#augmented=aug.augment_image(images[1])
#imageio.imwrite("./rotated.png",augmented)



"""
while c<=len(images):
    augmented=aug.augment_image(images[c])
    imageio.imwrite("./AdditiveGaussianNoise/"+str(c)+".png",augmented)
    c+=1
"""    


"""
seq = iaa.Sequential([
    iaa.CropAndPad(percent=(-0.2, 0.2), pad_mode="edge"),  # crop and pad images
    iaa.AddToHueAndSaturation((-60, 60)),  # change their color
    iaa.ElasticTransformation(alpha=90, sigma=9),  # water-like effect
    iaa.CoarseDropout((0.01, 0.1), size_percent=0.01)  # set large image areas to zero
], random_order=True)
c=0
for i in images:
    cv2.imwrite("len"+str(c)+".png",cv2.cvtColor((seq.augment_images(images))[c],
    cv2.COLOR_BGR2RGB))
    print("Photo #"+str(c))
    ia.imshow((seq.augment_images(images))[c])
    c+=1
print("Program terminated.")
  

seq2 = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])
c=0
images2 = seq2.augment_images(images)
for i in images2:
    cv2.imwrite("len"+str(c)+".png",cv2.cvtColor((seq2.augment_images(images2))[c],
                          cv2.COLOR_BGR2RGB))
"""  
