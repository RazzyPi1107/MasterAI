import shutil, os
import yfinance as yf
import pandas as pd
import time
import schedule
import datetime
from datetime import date, timedelta
import numpy as np
from pandas import ExcelWriter
import csv
import requests

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps
import PIL
import os
import time
import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
import argparse
import os
import random
from PIL import Image



files = ['00_DayCandleSrick.png', "02_RSI_DayCandleSrick.png", '03_MACD_DayCandleSrick.png','04_ToDay_Chart.png','05_Pivot_Day_Chart.png','07_Call_Nifty.png','08_Puts_Nifty.png','06_TopGailLose.png', '09_FiiDii.png']
for f in files:
    shutil.copy(f, 'Collage')

tod = datetime.datetime.now()









OutputFile = "Collage_Title.png"
ImgWidth = 1400
IntHt = 1080
folder = "Collage"
shuffle = False

def make_collage(images, filename, width, init_height):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    if not images:
        print('No images for collage found!')
        return False

    margin_size = 2
    # run until a suitable arrangement of images is found
    while True:
        # copy images to images_list
        images_list = images[:]
        coefs_lines = []
        images_line = []
        x = 0
        while images_list:
            # get first image and resize to `init_height`
            img_path = images_list.pop(0)
            img = Image.open(img_path)
            img.thumbnail((width, init_height))
            # when `x` will go beyond the `width`, start the next line
            if x > width:
                coefs_lines.append((float(x) / width, images_line))
                images_line = []
                x = 0
            x += img.size[0] + margin_size
            images_line.append(img_path)
        # finally add the last line with images
        coefs_lines.append((float(x) / width, images_line))

        # compact the lines, by reducing the `init_height`, if any with one or less images
        if len(coefs_lines) <= 1:
            break
        if any(map(lambda c: len(c[1]) <= 1, coefs_lines)):
            # reduce `init_height`
            init_height -= 10
        else:
            break

    # get output height
    out_height = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            out_height += int(init_height / coef) + margin_size
    if not out_height:
        print('Height of collage could not be 0!')
        return False

    collage_image = Image.new('RGB', (width, int(out_height)), (35, 35, 35))
    # put images to the collage
    y = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            x = 0
            for img_path in imgs_line:
                img = Image.open(img_path)
                # if need to enlarge an image - use `resize`, otherwise use `thumbnail`, it's faster
                k = (init_height / coef) / img.size[1]
                if k > 1:
                    img = img.resize((int(img.size[0] * k), int(img.size[1] * k)), Image.ANTIALIAS)
                else:
                    img.thumbnail((int(width / coef), int(init_height / coef)), Image.ANTIALIAS)
                if collage_image:
                    collage_image.paste(img, (int(x), int(y)))
                x += img.size[0] + margin_size
            y += int(init_height / coef) + margin_size
    collage_image.save(filename)
    return True






if not ImgWidth or not IntHt:
    parse.print_help()
    exit(1)

# get images
FolderPath = r"C:\01_PythonCodes\Gr8\MasterAI\Collage"
files = [os.path.join(FolderPath, fn) for fn in os.listdir(FolderPath)]
images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
if not images:
    print('No images for making collage! Please select other directory with images!')
    exit(1)

# shuffle images if needed
if shuffle:
    random.shuffle(images)

print('Making collage...')
res = make_collage(images, OutputFile, ImgWidth, IntHt)
if not res:
    print('Failed to create collage!')
    exit(1)
print('Collage is ready!')





m3=str (tod.strftime("%b"))
d3=str (tod.strftime("%d"))
y3=str (tod.strftime("%Y"))
today2 = str(d3)+str(' - ')+str(m3) +str(' - ')+str(y3)
text =  str(today2)

OutputFile = "Collage_Title.png"

Image1 = Image.open('PlainBackground.png').convert('RGBA')


image2 = Image.open(OutputFile).convert('RGBA')


print (Image1.size)
print (image2.size)

px, py = 250, 15
sx, sy = image2.size
Image1.paste(image2, (px, py, px + sx, py + sy), image2)

width = Image1.size[0]
height = Image1.size[1]
for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = Image1.getpixel((i,j))
        #print(data) #(255, 255, 255)
        if (data[0]==35 and data[1]==35 and data[2]==35):
            Image1.putpixel((i,j),(18, 0, 82))

Image1.save("TEST2.png", quality=100)

Image1 = Image.open("TEST2.png").convert('RGBA')
image2 = Image.open('Verticaleside1.png').convert('RGBA')

print (image2.size)

px, py = 5, 5
sx, sy = image2.size
Image1.paste(image2, (px, py, px + sx, py + sy), image2)


Image1.save("TEST2.png", quality=100)

Image1 = Image.open("TEST2.png").convert('RGBA')

font = ImageFont.truetype('Bold.ttf', size=135)
text_layer = Image.new('L', (1080, 1080))
draw = ImageDraw.Draw(text_layer)
image3 = PIL.Image.new('RGBA', (1200, 1200), (255, 255, 255, 255))
draw2 = ImageDraw.Draw(image3)
draw2.text((40, 5), text=text, font=font, fill= '#120052')

Image2copy = image3.rotate((90), expand=0)
Image1.paste(Image2copy, (1750, -120))

Image1.save("0000000000_TITILE.png", quality=100)

