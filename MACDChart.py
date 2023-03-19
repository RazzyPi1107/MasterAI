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
import seaborn as sns
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


Image1 = Image.open('PlainBackground.png').convert('RGBA')


image2 = Image.open('01_DayCandleSrick_half.png').convert('RGBA')

image2 = image2.resize((1920,540))


print (Image1.size)
print (image2.size)

px, py = 0, 0
sx, sy = image2.size
Image1.paste(image2, (px, py, px + sx, py + sy), image2)

Image1.save("TEST2.png", quality=100)

Image1 = Image.open("TEST2.png").convert('RGBA')
image2 = Image.open('03_MACD_DayCandleSrick.png').convert('RGBA')
image2 = image2.resize((1920,540))

print (image2.size)

px, py = 0, 540
sx, sy = image2.size
Image1.paste(image2, (px, py, px + sx, py + sy), image2)


Image1.save("03A_MACD_modified.png", quality=100)

