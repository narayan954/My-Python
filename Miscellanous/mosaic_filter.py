"""
This Program is not my own and i am only using it for learning purpose
"""

"""
This program generates the Photographic Mosaic based on the original image.
"""

from simpleimage import SimpleImage
import random

"""
INSTRUCTIONS for USE:
RESOLUTION controls how many 'columns' are in the mosaic.
MINI_IMAGE_FACTOR controls how small the repeating image is (1 = original size, 10 = one-tenth the size).
GLOBAL_IMAGE_NAME points to the background image you want to see.
LOCAL_IMAGE_NAME points to the cell image.
COLOUR_LEAK varies how much of the background colour appears in the foreground (0 = none, 1+ = a lot).
"""
#Change these values
RESOLUTION = 20
MINI_IMAGE_FACTOR = 25
LOCAL_IMAGE_NAME = 'images/simba-sq.jpg'
GLOBAL_IMAGE_NAME = 'images/simba-sq.jpg'

#Global Parameters defined here
COLOUR_LEAK = 1.3
X_LATTICE = RESOLUTION
Y_LATTICE = RESOLUTION
LOCAL_IMAGE_SIZE = 222
local_image = SimpleImage(LOCAL_IMAGE_NAME)
LOCAL_IMAGE_WIDTH = local_image.width
LOCAL_IMAGE_HEIGHT = local_image.height
MINI_IMAGE_WIDTH = int(LOCAL_IMAGE_WIDTH / MINI_IMAGE_FACTOR)
MINI_IMAGE_HEIGHT = int(LOCAL_IMAGE_HEIGHT / MINI_IMAGE_FACTOR)
FINAL_WIDTH = X_LATTICE * MINI_IMAGE_WIDTH
FINAL_HEIGHT = Y_LATTICE * MINI_IMAGE_HEIGHT


def main():
    #A final, stitched image of all local_images
    final_image = SimpleImage.blank(FINAL_WIDTH,FINAL_HEIGHT)
    #local_image is the source to creat the unit
    local_image = SimpleImage(LOCAL_IMAGE_NAME)
    #mini_image is the unit, created from local_image and mapped to final_image using information from global_image
    mini_image = mini(local_image)
    #global_image is the source to form the overall heat map
    global_image = SimpleImage(GLOBAL_IMAGE_NAME)

    global_image_x_offset = int(global_image.width / X_LATTICE)
    global_image_y_offset = int(global_image.height / Y_LATTICE)

    for j in range (Y_LATTICE):
        for i in range (X_LATTICE):
            final_image_x_start = i * MINI_IMAGE_WIDTH
            final_image_y_start = j * MINI_IMAGE_HEIGHT
            mini_image_altered = alter_mini_image(global_image,mini_image,global_image_x_offset,global_image_y_offset,i,j)
            final_image = stitch(final_image,mini_image_altered,final_image_x_start,final_image_y_start)
    final_image.show()

def alter_mini_image(global_image,mini_image,global_image_x_offset,global_image_y_offset,i_master,j_master):
    return_image = mini_image
    return_image = SimpleImage.blank(mini_image.width,mini_image.height)
    for j in range (mini_image.height):
        for i in range (mini_image.width):
            return_image.set_pixel(i,j,mini_image.get_pixel(i,j))
    
    """
    This loop goes through an equivalent box on global and reads average colour brightness
    """
    global_box_total_green = 0
    global_box_total_red = 0
    global_box_total_blue = 0
    iteration_counter = 0
    for j in range (j_master * global_image_y_offset , (j_master + 1) * global_image_y_offset - 1):
        for i in range (i_master * global_image_x_offset , (i_master + 1) * global_image_x_offset - 1):
            pixel_global_box = global_image.get_pixel(i,j)
            global_box_total_green += pixel_global_box.green
            global_box_total_red += pixel_global_box.red
            global_box_total_blue += pixel_global_box.blue
            iteration_counter += 1
    global_box_average_green = global_box_total_green//iteration_counter
    global_box_average_red = global_box_total_red//iteration_counter
    global_box_average_blue = global_box_total_blue//iteration_counter
    global_box_average = (global_box_average_green + global_box_average_red + global_box_average_blue)/3

    """
    for j in range (mini_image.height):
        for i in range (mini_image.width):
            #k = int(i * global_image.width / mini_image.width)
            #l = int(j * global_image.height / mini_image.height)
            pixel_global = global_image.get_pixel(k,l)
            pixel_return = return_image.get_pixel(i,j)
            average = int((pixel_global.red + pixel_global.blue + pixel_global.green)/3)
            intensity = 2*average/255
            pixel_return.red = intensity * pixel_global.red * random.random()*2 #######################
            pixel_return.blue = intensity * pixel_global.blue
            pixel_return.green = intensity * pixel_global.green
            return_image.set_pixel(i,j,pixel_return)
    """
    for pixel in return_image:
        pixel.green = pixel.green * ((1-COLOUR_LEAK) * global_box_average / 255 + COLOUR_LEAK * global_box_average_green / 255)
        pixel.red = pixel.red * ((1-COLOUR_LEAK) * global_box_average / 255 + COLOUR_LEAK * global_box_average_red / 255)
        pixel.blue = pixel.blue * ((1-COLOUR_LEAK) * global_box_average / 255 + COLOUR_LEAK * global_box_average_blue / 255)
    return return_image

def mini(local_image):
    mini_image_width = MINI_IMAGE_WIDTH
    mini_image_height = MINI_IMAGE_HEIGHT
    return_img = SimpleImage.blank(mini_image_width,mini_image_height)
    for j in range (MINI_IMAGE_HEIGHT):
        for i in range (MINI_IMAGE_WIDTH):
            return_img.set_pixel(i,j,local_image.get_pixel(int(i * MINI_IMAGE_FACTOR), int(j * MINI_IMAGE_FACTOR)))
    return return_img

def stitch(final_image,local_image,x_offset,y_offset):
    for j in range (local_image.height):
        for i in range (local_image.width):
            final_image.set_pixel(i + x_offset, j + y_offset, local_image.get_pixel(i,j))
    return final_image

def make_recolored_patch(img,red_scale, green_scale, blue_scale):
    novel_img = SimpleImage.blank(img.width,img.height)
    for j in range (img.height):
        for i in range (img.width):
            novel_img.set_pixel(i,j,img.get_pixel(i,j))
    for pixel in novel_img:
        pixel.red = red_scale * pixel.red
        pixel.blue = blue_scale * pixel.blue
        pixel.green = green_scale * pixel.green
    return novel_img


if __name__ == '__main__':
    main()
