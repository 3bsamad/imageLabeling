# Remove Background 
This simple code contains a Python method which, given an image as an input, extracts the background (Green Screen) and leaves the user with the foreground object, and a fully black background. 

# Prequisites
You should already know the values of the pixels which you want to remove i.e. the RGB values of the background.

You also need the PIL (Python Image Library)

```pip install pillow```

# Change Mask 
This code changes the color of the mask created around the object to red by default. By Changing the RGB values, you can create a mask of any desired color. 
