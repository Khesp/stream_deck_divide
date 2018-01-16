# Stream Deck Divide

This plugin for Gimp divides a given image so that it can be used as a wallpaper on the Elgato Stream Deck.  
__Example:__  
Original image on the left and modified image on the right (looks a whole better in reality):  
![Example](/readme_images/example.png)
## How it works

The plugin takes an image an checks if it has the right ratio (5:3). If not, it crops the image (from the center) to the needed ratio and then divides it into 5 X 3 pieces. The divided images will be saved as PNGs in the same directory as the original image.

## How to install

Just copy the stream_deck_divide.py file into the python plugin folder of Gimp and restart it. For Windows it should be something like C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

## How to use

Open an image and crop it manually to a 5:3 ratio or let the plugin do it for you. The advantage of the manual method is, that you can choose the exact area for cropping the image (the plugin crops it always from the center). To crop it manually just choose the crop tool (shift + c) in Gimp, click the "Fixed" box in the tool options and set the aspect ratio to 5:3.

![Gimp Crop Tool](/readme_images/gimp_crop.png)

Draw a square with the tool and crop the selected area with a single click on it.  
Now go to "Filters" -> "Stream Deck" -> "Divide Image"  
If you cropped the image manually, the plugin will divide the image and save the resulting images in the folder of the original image.
Otherwise it will crop the image and then do the same.  
You shoud now find additional 15 files in the folder of the original image. They should be named liked [file name]-[line number]-[column number].png  
You can now create e.g. hotkeys on your Stream Deck and drag the images in the right order on the 15 hotkeys. You can use the numbers of the files for orientation. So [file_name]-0-0.png belongs to the upper left, [file_name]-0-1.png to the middle left... and so on (see picture).  

![Gimp Crop Tool](/readme_images/stream_deck_layout.png)
