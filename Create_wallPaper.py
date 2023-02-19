from turtle import screensize
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import ctypes
import time

screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
width, height = screensize

img = Image.new(mode='RGB', size=screensize)
image_editable = ImageDraw.Draw(img)
title_Font = ImageFont.truetype('arial.ttf', 30)

def setWallPaper():
    path = r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


def create_wallpaper():

    shape = [(width, height), (0, 0)]
    image_editable = ImageDraw.Draw(img)
    image_editable.rectangle(shape, fill=0)
    img.save(r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg')



    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    text_to_display = current_time

    w,h = image_editable.textsize(text_to_display, font=title_Font)
    image_editable.text((((width-w)/2, (height-h)/2)), text_to_display, font=title_Font)
    img.save(r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg')



# def black_wall():
#     img_1 = Image.new(mode='RGB', size=screensize)
#     img_1.save(r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg')
#     path = r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg'
#     SPI_SETDESKWALLPAPER = 20
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


if __name__ == '__main__':

    while True:
        create_wallpaper()
        setWallPaper()
        time.sleep(1)



    
