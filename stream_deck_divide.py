import os
from gimpfu import *

def stream_deck_divide(image, drawable) :
    stream_deck_ratio = 5.0/3
    width = pdb.gimp_image_width(image)
    height = pdb.gimp_image_height(image)
    sd_width = 0
    sd_height = 0
    crop_x = 0
    crop_y = 0
    ratio = float(width)/height
    
    if ratio > stream_deck_ratio:
        sd_width = height * 5.0 / 3
        sd_height = height
        crop_x = (width - int(round(sd_width))) / 2
        pdb.gimp_image_crop(image, sd_width, sd_height, crop_x, 0)
    elif ratio < stream_deck_ratio:
        sd_height = width * 3.0 / 5
        sd_width = width
        crop_y = (height - int(round(sd_height))) / 2
        pdb.gimp_image_crop(image, sd_width, sd_height, 0, crop_y)
    else:
        sd_width = width
        sd_height = height
        
    pdb.script_fu_guide_new_percent(image, drawable, 0, 33.3)
    pdb.script_fu_guide_new_percent(image, drawable, 0, 66.6)
    pdb.script_fu_guide_new_percent(image, drawable, 1, 20)
    pdb.script_fu_guide_new_percent(image, drawable, 1, 40)
    pdb.script_fu_guide_new_percent(image, drawable, 1, 60)
    pdb.script_fu_guide_new_percent(image, drawable, 1, 80)  
    image_count, image_ids = pdb.plug_in_guillotine(image, drawable)
    
    for i in range(0, 15):
        file_list = gimp.image_list()[i]
        file = pdb.gimp_image_get_filename(file_list)
        file_png = os.path.splitext(file)[0] + ".png"
        pdb.file_png_save(file_list, file_list.active_drawable, file_png, file_png, 0, 0, 0, 0, 0, 0, 0)
        
register(
    "python-fu-stream-deck-divide",
    "Stream Deck",
    "Divides a given image into 3 x 15 pieces with 5 : 3 ratio.",
    "Khesp",
    "copyright 2018, Khesp",
    "2018",
    "<Image>/Filters/Stream Deck/Divide Image",
    "*",
    [],
    [],
    stream_deck_divide)

main()