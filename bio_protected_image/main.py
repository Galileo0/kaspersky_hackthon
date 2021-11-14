# kaspersky 
# Author: Ahmed Zakaria Mohamed
# Bio Protected Image

import bpi

def main():
    bpi_obj = bpi.bio_protected_image() #object
    image = bpi_obj.capture_image()
    #print(image)
    bpi_obj.view_image(image)
    bpi_obj.load_image(image)
    bpi_obj.protect_image()

main()
