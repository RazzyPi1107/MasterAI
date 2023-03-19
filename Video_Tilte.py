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
from time import strftime
import telepot
from telepot.loop import MessageLoop
import time
import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
import gtts
from playsound import playsound
import shutil, os

df2 = pd.read_excel('0000_Final_Final_Title.xlsx')

files = ['0000000000_TITILE.png',"000_Upload_This.mp4",'0000_Final_Final_Title.xlsx']
for f in files:
    shutil.copy(f, 'UPLOAD')



#df1['thisssayer'][]

TITLESS = str((df2['Heading'][0]))  + str((df2['Heading'][1])) + str(" | ") + str((df2['Heading'][2]))

print (TITLESS)