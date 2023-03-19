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
from nsepython import *
import matplotlib.pyplot as plt
import numpy as np

#print(nse_fiidii())
plt.style.use('cyberpunk')
plt.figure(figsize=(16, 9),facecolor='#120052', edgecolor="white")

ax = plt.axes()
ax.set_facecolor('#120052')



bb = nse_fiidii()
bb.to_csv("fiiii.csv")
df = pd.read_csv ('fiiii.csv')
#print (df.dtypes)
#print (df['buyValue'])




plt.barh(df['category'], df['buyValue'],align='center', color = "#26FE0C", label = 'DII', height = .5 , edgecolor = "#008933")
plt.barh(df['category'], (-1*df['sellValue']), align='center', color = "#FB1E0F", label = 'FII', height = .5, edgecolor = "#890000")
plt.barh(df['category'], (df['netValue']), align='center', color = "#00FFF2", label = 'FII', height = 0.4, alpha =1, edgecolor = "#2D38FF")
plt.axvline(x=0, color ="white", linestyle = "dashed")

for i in range (0, len(df)):
    plt.text((df['buyValue'][i]),df['category'][i], str("Buy: ")+str(int((df['buyValue'][i]))), horizontalalignment = "center", fontsize = 18, color= "w", bbox=dict(boxstyle="larrow,pad=0.3", facecolor="#006F06", edgecolor='yellow'), fontweight="bold", rotation =-90 )
    plt.text((-1*df['sellValue'][i]), df['category'][i], str("Sell: ")+str(int((df['sellValue'][i]))), horizontalalignment = "center", fontsize = 18, color= "w", bbox=dict(boxstyle="larrow,pad=0.3", facecolor="#800000", edgecolor='yellow'),  fontweight="bold", rotation = 90)
    plt.text((df['netValue'][i]), df['category'][i], str("Net: ")+str(int((df['netValue'][i]))), horizontalalignment = "center", fontsize = 22, color= "w", bbox=dict(boxstyle="sawtooth,pad=0.3", facecolor="#540080", edgecolor='yellow'),  fontweight="bold", rotation =0)


# setting label of y-axis

plt.grid(False)
#plt.yticks([])
plt.xticks([])
plt.yticks(fontsize = 25)

# setting label of x-axis

plt.title("FII/DII trading activity on NSE,BSE and MSEI in Capital Market Segment(In Rs. Crores)", fontsize = 18)
#plt.show()
filename =  str("09_FiiDii")+str('.png')
plt.savefig(filename, facecolor='#120052')

ListA=[]
ListB=[]

ListA.append("FII Buy")
ListB.append(int(df['buyValue'][0]))

ListA.append("FII Sell")
ListB.append(int(df['sellValue'][0]))

ListA.append("FII Net")
ListB.append(int(df['netValue'][0]))

ListA.append("DII Buy")
ListB.append(int(df['buyValue'][1]))

ListA.append("DII Sell")
ListB.append(int(df['sellValue'][1]))

ListA.append("DII Net")
ListB.append(int(df['netValue'][1]))



datab = {'Name': ListA, 'Value': ListB}
dffii = pd.DataFrame(datab)
#print (dffii)
dffii.to_csv("00_FIIDII.csv")

print ("FII DII Data Generated.")