from turtle import screensize
from PIL import Image, ImageFont, ImageDraw
import ctypes

screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

width, height = screensize

img = Image.new(mode='RGB', size=screensize)
image_editable = ImageDraw.Draw(img)
title_Font = ImageFont.truetype('arial.ttf', 30)
text_to_display = 'Hello World'

w,h = image_editable.textsize(text_to_display, font=title_Font)
image_editable.text((((width-w)/2, (height-h)/2)), text_to_display, font=title_Font)

img.save(r'C:\Users\atish\Desktop\programming\python\Wallpaper_with_python\image.jpg')