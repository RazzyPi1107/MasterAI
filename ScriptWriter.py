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
import aspose.words as aw

df1 = pd.read_excel('0000_Final_Read_script.xlsx')

dll = len (df1)
##################################################################### Intro
scripty = " "
start = 0
end = 1
for i in range (start,dll):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)

# create document object
doc = aw.Document()

# create a document builder object
builder = aw.DocumentBuilder(doc)

# add text to the document
builder.write(scripty)

# save document
doc.save("ZZTops.docx")