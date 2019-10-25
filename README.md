# Image Labeling
Labeling images for a dataset is of upmost importance in the field of machine learning. The goal here is building a dataset containing images, masks of the object to be recognised only, and a photo of both mask and original photo blended together. The motivation for this project is the [LabelMe Algorithm](https://github.com/wkentaro/labelme)

# Remove Background 
This simple code contains a Python method which, given an image as an input, extracts the background (Green Screen) and leaves the user with the foreground object, and a fully black background. 

# Prequisites
You should already know the values of the pixels which you want to remove i.e. the RGB values of the background.

You also need the PIL (Python Image Library)

```pip install pillow```

# Change Mask 
The file ```changeMask.py``` changes the color of the mask created around the object to red by default. By Changing the RGB values, you can create a mask of any desired color. 

# Blend Photos
The file```blendPhotos.py``` is a simple code for the linear blending of two photos. You can use the resultant mask from ```changeMask.py``` and blend it using ```blendPhotos.py``` with the original image from which the mask was created (preferably in grayscale). This results in a file which is labelled using a light red color. 
