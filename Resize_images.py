"""Robert Walczak
Program converts images to JPG and resizes them. Saves inplace - will override original."""

from PIL import Image
import os, sys
import glob

root_dir = "C:\\Users\\rewal\\PycharmProjects\\Toy_MNIST\\Testing_images\\" #set this as your working directory


for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True): # dont change anything here
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((500,500), Image.ANTIALIAS) # change 500,500 to what ever size you need
    imResize.save(filename , 'JPEG', quality=90)