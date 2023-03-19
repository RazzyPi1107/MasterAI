#######################################

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
plt.style.use('cyberpunk')

bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'

SymbolNS ='^NSEBANK'

bb = yf.Ticker(SymbolNS)
bb = bb.history('7d')
lenb = len (bb)
lenc = lenb -2

previousClose = bb["Close"][lenc]


file = 'Dates.csv'
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV :

        today = row[1]
        yesterday = row[2]
        Tomm = row[3]



SymbolNS ='^NSEBANK'
aa = yf.download(SymbolNS, start=today , end=Tomm, interval = "1m",progress=False)
#print (aa)


aa['30MAM'] = aa.Close.rolling(20).mean() #Bollineger Band mean
aa['30MASD'] = aa.Close.rolling(20).std() #Bollineger Band std dev

aa['Bub'] = aa['30MAM'] + (aa['30MASD'] *2) #Bollineger  Upper Band
aa['Blb'] = aa['30MAM'] - (aa['30MASD'] *2) #Bollineger Lower Band

aa['ShortEMA'] =aa.Close.ewm(span=12, adjust=False).mean()
# long term EMA
aa['LongEMA'] = aa.Close.ewm(span=26, adjust=False).mean()
# MACD line
aa['MACD'] = aa['ShortEMA'] - aa['LongEMA']
# MACD Singal line

aa['signal'] = aa['MACD'].ewm(span=9, adjust=False).mean()
nkm = aa['signal'].shape[0]
aa['Nan']= np.nan
aa ['Calling']=aa['MACD']-aa['signal']
# 50 EMA : Beep Boop Strategy
aa['EMA50'] = aa.Close.ewm(span=50, adjust=False).mean()
aa['EMA200'] = aa.Close.ewm(span=200, adjust=False).mean()

def computeRSI (data, time_window):

    #R
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]

    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]

    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()

    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi


aa['RSI'] = computeRSI(aa['Close'], 14)

aa['dife']=aa['Close'].diff()

aa['50MA'] = aa.Close.rolling(50).mean()  # 50 day moving avg
aa['200MA'] = aa.Close.rolling(200).mean()  # 200 day moving avg
aa['52WH'] = aa.High.rolling(256).max()  # 256 is number of rows
aa['52WL'] = aa.Low.rolling(256).min()  # 256 is number of rows
aa['%ofL'] = round(aa['Close'] / aa['52WL'], 2)  # 52Week Low from that day
aa['%ofH'] = round(aa['Close'] / aa['52WH'], 2)  # 52Week High from that day
aa['30MAM'] = aa.Close.rolling(20).mean()  # Bollineger Band mean
aa['30MASD'] = aa.Close.rolling(20).std()  # Bollineger Band std dev
aa['50MAH'] = aa.Close.rolling(50).max()  # 50 is number of rows
aa['50MAL'] = aa.Close.rolling(50).min()  # 50 is number of rows

aa['Bub'] = aa['30MAM'] + (aa['30MASD'] * 2)  # Bollineger  Upper Band
aa['Blb'] = aa['30MAM'] - (aa['30MASD'] * 2)  # Bollineger Lower Band
aa['BBlwratio'] = aa['30MAM'] - aa['Blb']
aa['BBPrratio'] = aa['Close'] - aa['Blb']
aa['BBratio'] = aa['BBPrratio'] / aa['BBlwratio']

aa['Volumem'] = aa.Volume.rolling(3).mean()  # 50 day moving avg
aa['Volumesd'] = aa.Volume.rolling(2).std()  # 50 day moving avg
aa['Volumesdm'] = aa.Volumesd.rolling(3).mean()  # 50 day moving avg
aa['Doji'] = aa['Close'] - aa['Open']  # Cal Doji location
# short term EMA
aa['ShortEMA'] = aa.Close.ewm(span=12, adjust=False).mean()
# long term EMA
aa['LongEMA'] = aa.Close.ewm(span=26, adjust=False).mean()
# MACD line
aa['MACD'] = aa['ShortEMA'] - aa['LongEMA']
# MACD Singal line

aa['signal'] = aa['MACD'].ewm(span=9, adjust=False).mean()
nkm = aa['signal'].shape[0]
aa['Nan'] = np.nan
aa['Calling'] = aa['MACD'] - aa['signal']
# 50 EMA : Beep Boop Strategy
aa['EMA50'] = aa.Close.ewm(span=50, adjust=False).mean()
aa['1D'] = aa.Close.diff()
aa['v1d'] = aa['1D'] * aa['Volume']
aa['v1dd'] = aa.v1d.diff()

aa['Time'] = aa.index
#print (aa['Time'])

#fig,(ax1) = plt.subplots(1, sharex=True )

fig, ax1 = plt.subplots()
fig.set_size_inches(16, 9)
fig.patch.set_facecolor('#4d0026')
ax1.set_facecolor('#4d0026')
#plt.tight_layout()

#aa[['200MA']].plot(ax=ax1, legend=False, linestyle='dashed', color='c',linewidth=.3)  # Remove legend and on primary axis
#aa[['50MA']].plot(ax=ax1, legend=False, linestyle='dashed', color='m', linewidth=.3)
#aa[['EMA50']].plot(ax=ax1, legend=False, linestyle='dotted', color='r', linewidth=1)
# aa[['Open']].plot(ax=ax,legend=False, color='b', linewidth= .3 )
# aa[['High']].plot(ax=ax,legend=False, color='g', linewidth= .3 )
# aa[['Low']].plot(ax=ax,legend=False, color='r', linewidth= .2 )
#aa[['Close']].plot(ax=ax1, legend=False, color='#ff00a0', linewidth=1.1)
#aa[['30MAM', 'Bub', 'Blb']].plot(ax=ax1, legend=False, color='#FF6A00', linestyle='solid', linewidth=0.8)
# aa[['52WH','52WL']].plot(ax=ax,legend=False, color='#FF6A00', linestyle='dotted',linewidth= 0.008, alpha = .005)

#mplcyberpunk.make_lines_glow()

aa[['Close']].plot(ax=ax1, legend=False, color='w', linewidth=.3)

filnamor = str(SymbolNS) + str('.csv')

# aa.to_csv(filnamor) # Save as CSV file

nn = aa.shape[0]
nm = nn - 1
highL = (aa["High"]).max()
LowL = (aa["Low"]).min()

#print (highL,LowL)

dl = len (aa)

for i in range (0, dl):
    if (aa["High"][i])>=highL:

        xHh = aa["Time"][i]
        #print(xHh)

for i in range (0, dl):
    if (aa["Low"][i]) <=LowL:

        xLl = aa["Time"][i]
        #print(xLl)

x_axis = aa.index.get_level_values(0)

dm = dl - 1
Clt = aa["Time"][dm]
ClPP = aa["Close"][dm]


Olt = aa["Time"][0]
OlPP = aa["Open"][0]

close_plus_10 = aa["Time"][dm] - timedelta(minutes = 5)
open_min_10 = aa["Time"][0] - timedelta(minutes = 5)


#print (OlPP, ClPP)





#define width of candlestick elements
width = 0.9
width2 = .08

#define up and down prices
up = aa[aa.Close>=aa.Open]
down = aa[aa.Close<aa.Open]

#define colors to use
col1 = '#03FF29'
col2 = '#FF033E'

#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)


plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)













PrevCloseV = round(previousClose,0)
OpenV = round(OlPP,0)
LowV = round(LowL,0)
HighV = round(highL,0)
CloseV = round(ClPP,0)
GapV = OpenV - PrevCloseV
GapVV = abs(GapV)
TotalDel =  CloseV - PrevCloseV
TotalDelV = abs(TotalDel)
PP =   int (( HighV + CloseV + LowV ) / 3)
R1 =  ( 2 * PP ) - LowV
S1 =  ( 2 * PP ) - HighV
R2 =  PP + (HighV-LowV)
S2 =  PP - (HighV-LowV)




formulapivot ='''
Pivot point (PP) = (High + Low + Close) / 3

First level support and resistance:

First resistance (R1) = (2 x PP) – Low

First support (S1) = (2 x PP) – High

Second level of support and resistance:

Second resistance (R2) = PP + (High – Low)

Second support (S2) = PP – (High – Low)

'''

CloseDir = "Down"
if TotalDel >= 0:
    CloseDir = "Up"


GapD = "Down"
if GapV >= 0:
    GapD = "Up"
#print (GapD)


if xHh < xLl:
    HighLow = "HighLow"
    #print ("First")

if xHh > xLl:
    HighLow = "LowHigh"
    #print("second")



ax1.axhline(highL, color='#19FF50', linestyle='dotted', linewidth=1, alpha=0.8)
ax1.axhline(LowL, color='#FF1919', linestyle='dotted', linewidth=1, alpha=0.8)
ax1.axhline(OlPP, color='#01FFFF', linestyle='dotted', linewidth=1, alpha=0.8)
ax1.axhline(ClPP, color='#EB15DC', linestyle='dotted', linewidth=1, alpha=0.8)
ax1.axhline(previousClose, color='#808080', linestyle='dotted', linewidth=1, alpha=0.8)

ax1.axhline(PP, color='#0000FF', linestyle='solid', linewidth=2, alpha=0.8)
ax1.axhline(R1, color='#0000FF', linestyle='solid', linewidth=2, alpha=0.8)
ax1.axhline(S1, color='#0000FF', linestyle='solid', linewidth=2, alpha=0.8)
ax1.axhline(R2, color='#0000FF', linestyle='solid', linewidth=2, alpha=0.8)
ax1.axhline(S2, color='#0000FF', linestyle='solid', linewidth=2, alpha=0.8)

# plt.text(fromdate, wh52, '52 Week High (100%)', fontsize = 8, style='italic', color='b')
# ax1.axhline(wl52, color='b', linestyle='solid', linewidth= 0.5, alpha = 0.8)
# plt.text(fromdate, wl52, '52 Week Low (0%)', fontsize = 8, style='italic', color='b')
plt.xticks(rotation=90)
ax1.set_title(SymbolNS)
plt.xlabel('Time')
# ax1.set_xlabel('Theta (radians)')
ax1.set_ylabel('Price')
# ax2.set_xlabel('Phi (radians)')


#ax1.tick_params(axis="x", direction="in", length=1, width=1, color="turquoise")
#ax1.tick_params(axis="y", direction="in", length=1, width=4, color="orange", labelrotation=90)
#ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.grid(axis="x", color="white", alpha=.2, linewidth=1, linestyle=":")
ax1.tick_params(axis='both', which='major', labelsize=10)

offset = 72

arrowprops = dict(
    arrowstyle="->", color ="r",
    connectionstyle="angle, angleA = 0, angleB = 90,\
    rad = 10")

ax1.annotate('display = (%.1f, %.1f)',
                   (100, highL), xytext=(0,0),
                   xycoords='figure pixels',
                   textcoords='offset points',
                   bbox=dict(boxstyle = "square",facecolor = "red", edgecolor='green'), arrowprops=arrowprops, color='white', backgroundcolor='k', fontweight="bold", fontsize=16)


ax1.text(xHh, (highL+7), (str('High: ')+str(HighV)), bbox=dict(boxstyle = "square",facecolor = "#00FF00", edgecolor='#154734'), fontsize=12, fontweight="bold", color ="k")
ax1.text(xLl, (LowL-9), (str('Low: ')+str(LowV)), bbox=dict(boxstyle = "square",facecolor = "#FF0000", edgecolor='#800500'), fontsize=12, fontweight="bold")
ax1.text(open_min_10, (OlPP+0), (str('Open: ')+str(OpenV)), bbox=dict(boxstyle = "square",facecolor = "#FFFF00", edgecolor='#FF6600'), fontsize=12, fontweight="bold",horizontalalignment = "right", color ="k")
ax1.text(close_plus_10, (ClPP+0), (str('Close: ')+str(CloseV)), bbox=dict(boxstyle = "square",facecolor = "#CC00FF", edgecolor='#FF00FF'), fontsize=12, fontweight="bold",horizontalalignment = "left")
ax1.text(open_min_10, (previousClose - 3), (str('Prev.Close: ')+str(PrevCloseV)), bbox=dict(boxstyle = "square",facecolor = "#D7D2CB", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "right", color ="k")
ax1.axvline(xHh, color= '#FFFF00', linestyle='dotted', linewidth= .5, alpha = 0.9)
ax1.axvline(xLl, color= '#FFFF00', linestyle='dotted', linewidth= .5, alpha = 0.9)


ax1.text(close_plus_10, (PP), (str('Pivot: ')+str(PP)), bbox=dict(boxstyle = "larrow",facecolor = "#778899", edgecolor='#0000FF'), fontsize=20, fontweight="bold", color ="w")
ax1.text(close_plus_10, (R1), (str('R1: ')+str(R1)), bbox=dict(boxstyle = "larrow",facecolor = "#0000FF", edgecolor='#0000FF'), fontsize=20, fontweight="bold", color ="w")
ax1.text(close_plus_10, (S1), (str('S1: ')+str(S1)), bbox=dict(boxstyle = "larrow",facecolor = "#0000FF", edgecolor='#0000FF'), fontsize=20, fontweight="bold",horizontalalignment = "left", color ="w")
ax1.text(close_plus_10, (R2), (str('R2: ')+str(R2)), bbox=dict(boxstyle = "larrow",facecolor = "#0000FF", edgecolor='#0000FF'), fontsize=20, fontweight="bold",horizontalalignment = "left", color ="w")
ax1.text(close_plus_10, (S2), (str('S2: ')+str(S2)), bbox=dict(boxstyle = "larrow",facecolor = "#0000FF", edgecolor='#0000FF'), fontsize=20, fontweight="bold",horizontalalignment = "left", color ="w")

ax1.text(open_min_10, (highL), (formulapivot), bbox=dict(boxstyle = "sawtooth",facecolor = "#0000FF", edgecolor='#0000FF', alpha = 0.7), fontsize=18, fontweight="bold",horizontalalignment = "left", verticalalignment  = "top", color ="w", alpha =0.9)



'''
# Setting up the parameters
xdata, ydata = 5, 0
xdisplay, ydisplay = ax1.transData.transform((xdata, ydata))

bbox = dict(boxstyle="round", fc="0.8",edgecolor='red', facecolor='k' )


offset = 72

# Annotation


ax1.annotate('display = (%.1f, %.1f)' % (xdisplay, ydisplay),
                   (xdisplay, ydisplay), xytext=(0.5 * offset, -offset),
                   xycoords='figure pixels',
                   textcoords='offset points',
                   bbox=dict(boxstyle = "square",facecolor = "red", edgecolor='green'), arrowprops=arrowprops, color='white', backgroundcolor='k', fontweight="bold", fontsize=16)

ax1.text(2, .4, "Text in a box",
        bbox=dict(boxstyle = "square",facecolor = "red", edgecolor='green'))


'''
Titls = str("Pivot Points for Next Day ")


plt.title(Titls, fontsize = 18)
#mplcyberpunk.make_lines_glow()

plt.savefig("05_Pivot_Day_ChartB.png", facecolor=fig.get_facecolor())

























Decri = ["Pivot", "R1", "S1", "R2", "S2"]

Valus= []
Valus.append(PP)
Valus.append(R1)
Valus.append(S1)
Valus.append(R2)
Valus.append(S2)




datab = {'Name': Decri, 'Value': Valus}
dpiv = pd.DataFrame(datab)
dpiv.to_csv("00_PivotDayValues.csv")
aa.to_csv("aaa.csv")


filnamor = str(SymbolNS)+str('.csv')
#dff.to_csv(filnamor)
#plt.show()
filename = str(SymbolNS)+str('.png')

plt.close("all")
plt.close()

plt.clf()

print ("Pivot Point Chart Data Generated.")