from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
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
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib import image
from dateutil.relativedelta import relativedelta, TH
from nsepython import *
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
import mplcyberpunk
from matplotlib.gridspec import GridSpec
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from numpy.random import rand
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator, LinearLocator, NullLocator)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df1 = pd.read_excel('0000_speechsB.xlsx')
print (df1['thisssayer'][3])
df3= df1
DECI = 00


############################################################################# Intraday values  Values
df00 = pd.read_csv ('00_DailyChartValues.csv')
print (df00)

dayz = ['सोमवार', 'मंगळवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार', 'रविवार']
n1 = int(df00['Value'][8])
dayday = dayz[n1]
print (dayday)
df3['thisssayer'][3]= dayday

df3['thisssayer'][5] = df00['Value'][7]
############# Candle

if df00['Value'][0]=="green":
    DECI = df1['Done'][33]

if df00['Value'][0] == "red":
    DECI = df1['Dtwo'][33]

df3['thisssayer'][33] = DECI

############### 50 MA
if df00['Value'][1]=="Above50andAbove200":
    DECI = df1['Dtwo'][36]

if df00['Value'][1] == "Below50andBelow200":
    DECI = df1['Done'][36]

if df00['Value'][1]=="Above50andBelow200":
    DECI = df1['Dthre'][36]

if df00['Value'][1] == "Below50andAbove200":
    DECI = df1['Dfou'][36]

df3['thisssayer'][36] = DECI

############### Bolinger

if df00['Value'][2]== "Above-upper":
    DECI = df1['Done'][38]

if df00['Value'][2] ==  "Below-lower":
    DECI = df1['Dtwo'][38]

if df00['Value'][2]=="Above-Middle-Below-Upper":
    DECI = df1['Dthre'][38]

if df00['Value'][2] == "Above-lower-Below-Middle":
    DECI = df1['Dfou'][38]

df3['thisssayer'][38] = DECI

############# RSI

df3['thisssayer'][41] = df00['Value'][3]


if df00['Value'][4]== "Overbought":
    DECI = df1['Done'][43]

if df00['Value'][4] ==  "Oversold":
    DECI = df1['Dtwo'][43]

if df00['Value'][4]=="Strong":
    DECI = df1['Dthre'][43]

if df00['Value'][4] == "Weak":
    DECI = df1['Dfou'][43]

df3['thisssayer'][43] = DECI

#######################  MACD

df3['thisssayer'][46] = df00['Value'][5]

#####

if df00['Value'][6]=="Down":
    DECI = df1['Done'][49]

if df00['Value'][6] == "Up":
    DECI = df1['Dtwo'][49]

df3['thisssayer'][49] = DECI


############################################################################# Day Values
df01 = pd.read_csv ('00_DayValues.csv')
print (df01)

df3['thisssayer'][7] = df01['Value'][0]
df3['thisssayer'][9] = df01['Value'][1]
df3['thisssayer'][11] = df01['Value'][2]

if df01['Value'][3]=="Up":
    DECI = df1['Done'][13]

if df01['Value'][3] == "Down":
    DECI = df1['Dtwo'][13]


df3['thisssayer'][13] = DECI

df3['thisssayer'][15] = df01['Value'][5]
df3['thisssayer'][17] = df01['Value'][4]


if df01['Value'][6]=="HighLow":
    DECI = df1['Done'][20]
    df3['thisssayer'][22] = "High"
    df3['thisssayer'][24] = "Low"

if df01['Value'][6] == "LowHigh":
    DECI = df1['Dtwo'][20]
    df3['thisssayer'][22] = "Low"
    df3['thisssayer'][24] = "High"


df3['thisssayer'][20] = DECI

df3['thisssayer'][26] = df01['Value'][7]

df3['thisssayer'][28] = str(df01['Value'][8]) + str(" points. म्हणजे ") + str(df01['Value'][10])

if df01['Value'][9]=="Up":
    DECI = df1['Done'][30]


if df01['Value'][9] == "Down":
    DECI = df1['Dtwo'][30]


df3['thisssayer'][30] = DECI


############################################################################# Gainer and Loser
df02 = pd.read_csv ('00_GainLose.csv')
pd.set_option('display.max_columns', None)
print (df02)

df3['thisssayer'][53] = df02['GreenS'][0]
df3['thisssayer'][55] = df02['Reds'][0]

df3['thisssayer'][58] = df02['Name'][0]
df3['thisssayer'][60] = df02['Perc'][0]

df3['thisssayer'][62] = df02['Name'][1]
df3['thisssayer'][64] = df02['Perc'][1]

df3['thisssayer'][68] = df02['Name'][9]
df3['thisssayer'][70] = df02['Perc'][9]

df3['thisssayer'][72] = df02['Name'][8]
df3['thisssayer'][74] = df02['Perc'][8]


############################################################################# FII DII
df03 = pd.read_csv ('00_FIIDII.csv')
pd.set_option('display.max_columns', None)
print (df03)

df3['thisssayer'][87] = df03['Value'][0]
df3['thisssayer'][89] = df03['Value'][1]
df3['thisssayer'][91] = abs(df03['Value'][2])

if df03['Value'][2] >0:
    DECI = df1['Done'][93]

if df03['Value'][2] <= 0:
    DECI = df1['Dtwo'][93]


df3['thisssayer'][93] = DECI


df3['thisssayer'][78] = df03['Value'][3]
df3['thisssayer'][80] = df03['Value'][4]
df3['thisssayer'][82] = abs(df03['Value'][5])

if df03['Value'][5] >0:
    DECI = df1['Done'][84]

if df03['Value'][5] <= 0:
    DECI = df1['Dtwo'][84]


df3['thisssayer'][84] = DECI






############################################################################# Option Chain Analysis  -- CALLS
df04 = pd.read_csv ('00_OptionValuesCall.csv')

pd.set_option('display.max_columns', None)
print (df04)

df3['thisssayer'][97] = int(df04['Value'][2])
df3['thisssayer'][99] = int(df04['Value'][4])
df3['thisssayer'][101] = int(df04['Value'][3])


############################################################################# Option Chain Analysis  -- PUTS
df05 = pd.read_csv ('00_OptionValuesPUTS.csv')

pd.set_option('display.max_columns', None)
print (df05)

df3['thisssayer'][104] = int(df05['Value'][2])
df3['thisssayer'][106] = int(df05['Value'][4])
df3['thisssayer'][108] = int(df05['Value'][3])


df3['thisssayer'][111] = int(df04['Value'][2])
df3['thisssayer'][113] = int(df05['Value'][2])

############################################################################# Pivot Points
df06 = pd.read_csv ('00_PivotDayValues.csv')
pd.set_option('display.max_columns', None)
print (df06)

df3['thisssayer'][116]= int(df06['Value'][0])
df3['thisssayer'][119]= int(df06['Value'][1])
df3['thisssayer'][121]= int(df06['Value'][3])
df3['thisssayer'][123]= int(df06['Value'][2])
df3['thisssayer'][125]= int(df06['Value'][4])






############################################################################# Save Excel

datatoexcel = pd.ExcelWriter('0000_Final_Read_script.xlsx')
df3.to_excel(datatoexcel)

# save the excel
datatoexcel.save()