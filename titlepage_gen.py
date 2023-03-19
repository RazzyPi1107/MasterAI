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




tod = datetime.datetime.now()










m3=str (tod.strftime("%b"))
d3=str (tod.strftime("%d"))
y3=str (tod.strftime("%Y"))
today2 = str(d3)+str(' - ')+str(m3) +str(' - ')+str(y3)
text =  str(today2)
#text ="13 - APR - 2022"

OutputFile = "04_ToDay_Chart.png"

Image1 = Image.open('PlainBackground.png').convert('RGBA')


image2 = Image.open(OutputFile).convert('RGBA')


print (Image1.size)
print (image2.size)

px, py = 200, 150
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

px, py = 0, 0
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

Image1.save("TEST2.png", quality=100)

Image1 = Image.open("TEST2.png").convert('RGBA')

text =''' | 2-Min | Nifty-50 | Report
'''

font = ImageFont.truetype('Bold.ttf', size=100)
text_layer = Image.new('L', (1080, 100))
draw = ImageDraw.Draw(text_layer)
image3 = PIL.Image.new('RGBA', (1400, 130), (255, 255, 255, 255))
draw2 = ImageDraw.Draw(image3)
draw2.text((5, 5), text=text, font=font, fill= '#120052')

Image2copy = image3.rotate((0), expand=0)
Image1.paste(Image2copy, (300, 10))

Image1.save("0000000000_TITILE.png", quality=100)

