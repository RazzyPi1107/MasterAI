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
import mplcyberpunk
from matplotlib.gridspec import GridSpec
import matplotlib.dates as mdates

rtr = 10
plt.style.use('cyberpunk')

SymbolNS ='^NSEBANK'

aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com

aa = aa.history('3y')
#print (aa)
j1 = aa.shape[0]

Tday =[]
Yday=[]
TommD = []
Tomm = datetime.date.today() + datetime.timedelta(days=1)
#print (Tomm)
#print (j1)
j2 = j1 -1
j3 = j1 -2
a2 = aa.index[j2]


Tomm3 = datetime.date.today() + datetime.timedelta(days=15)
Tomm34 = datetime.date.today() + datetime.timedelta(days=1)

y3=int (a2.strftime("%Y"))
m3=int (a2.strftime("%m"))
d3=int (a2.strftime("%d"))
h3=int (a2.strftime("%H"))

#print (y3,m3,d3)
today = str(y3)+str('-')+str(m3)+str('-')+str(d3)
a3 = aa.index[j3]


y13=int (a3.strftime("%Y"))
m13=int (a3.strftime("%m"))
d13=int (a3.strftime("%d"))
h13=int (a3.strftime("%H"))

yesterday = str(y13)+str('-')+str(m13)+str('-')+str(d13)
Tomm = datetime.date.today() + datetime.timedelta(days=1)

#print (y13,m13,d13)

Tday.append(today)
Yday.append(yesterday)
TommD.append(Tomm)

datab ={'Tday':Tday, 'Yday':Yday, 'Tomm':TommD}
dff = pd.DataFrame(datab)

#print (dff)

filnamor = str('Dates')+str('.csv')
dff.to_csv(filnamor)

aa.drop(columns=['Dividends', 'Stock Splits'], inplace=True)
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

aa['1D'] = aa.Close.diff()
aa['VD'] = aa.Close.diff()

aa['v1d'] = (aa['1D'] * aa['Volume'])

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

aa['Callm'] = aa.Calling.rolling(3).mean()
aa['Calld'] = aa.Calling.diff()
aa['Calld2'] = aa.Calling.diff()

'''
#print ("nkm",nkm)

for l in range (1,nkm):
    ##print(l)
    #print (aa['MACD'][l])
    aa.replace(to_replace = aa['Nan'][l], value =-99999)
    if aa['MACD'][l]> aa['signal'][l]:
        aa['Buy'][l]= aa['Close'][l]
        aa['Sell'][l]= 0

    if aa['MACD'][l]< aa['signal'][l]:
        aa['Sell'][l]= aa['Close'][l]
        aa['Buy'][l]= 0

'''


def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for m in range(0, len(signal)):
        if aa['MACD'][m] > aa['signal'][m]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(aa['Close'][m])
                flag = 1
            else:
                Buy.append(np.nan)
        elif aa['MACD'][m] < aa['signal'][m]:

            Buy.append(np.nan)
            if flag != 0:
                Sell.append(aa['Close'][m])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

'''
a = buy_sell(aa)
aa['SELL'] = a[0]
aa['BUY'] = a[1]
'''
aa.to_csv("aaaa.csv")



#print (aa.index.duplicated())


def computeRSI(data, time_window):
    # R
    diff = data.diff(1).dropna()  # diff in one field(one day)

    # this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[diff > 0]

    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[diff < 0]

    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg = up_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1, min_periods=time_window).mean()

    rs = abs(up_chg_avg / down_chg_avg)
    rsi = 100 - 100 / (1 + rs)
    return rsi


aa['RSI'] = computeRSI(aa['Close'], 14)
aa['Time'] = aa.index
dlen = len (aa)
dlm = dlen-60
dln = dlen-1
xlim1 = aa['Time'][dlm]
xlim2 = Tomm3

bb = aa.tail(60)
maxim = bb.Bub.max()
minm =  bb.Blb.min()
ylim2 = maxim
ylim1 = minm


dlb = dlen-1

d50 = int(aa["50MA"][dlb])
d200 = int(aa["200MA"][dlb])
dbolu = int(aa["Bub"][dlb])
dbolm = int(aa["30MAM"][dlb])
dboll = int(aa["Blb"][dlb])
dclose = int(aa["Close"][dlb])
drsi = int(aa["RSI"][dlb])
dopen = int(aa["Open"][dlb])
dmacd0 = int(aa["Calling"][dlb])
dmacd1 = int(aa["Calling"][dlb-1])








Canle = "green"
if dopen>= dclose:
    Canle = "red"


day50loc ="Error"

if dclose >= d50 and  dclose >= d200:
    day50loc = "Above50andAbove200"
if dclose <= d50 and dclose <= d200 :
    day50loc = "Below50andBelow200"
if dclose >= d50 and dclose <= d200:
    day50loc = "Above50andBelow200"
if dclose <= d50 and dclose >= d200:
    day50loc = "Below50andAbove200"


BBloc ="Error"

if dclose >= dboll and dclose <= dbolm:
    BBloc = "Above-lower-Below-Middle"

if dclose >= dbolm and dclose <= dbolu:
    BBloc = "Above-Middle-Below-Upper"

if dclose >= dbolu:
    BBloc = "Above-upper"

if dclose <= dboll:
    BBloc = "Below-lower"


rsiint = "Error"

if drsi <= 30:
    rsiint = "Oversold"

if drsi <= 70:
    rsiint = "Overbought"

if drsi < 70 and drsi > 50:
    rsiint = "Strong"

if drsi <= 50 and drsi > 30:
    rsiint = "Weak"


macdloc = "Green"
if dmacd0 <=0:
    macdloc = "Red"


macddir = "Down"
if dmacd0 > dmacd1:
    macddir = "Up"


################################################################################ ONLY NIFTY DAILY

fig,(ax1) = plt.subplots(1, sharex=True , sharey=False, constrained_layout=True)
fig.patch.set_facecolor('#4d0026')
fig.set_size_inches(16, 9)
ax1.set_facecolor('#4d0026')
plt.xlim(xlim1,xlim2)
plt.ylim(ylim1,ylim2)

ax1.text(Tomm34, d50 , (str('50 Day MA: ')+str(d50)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "m", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, d200 , (str('200 Day MA: ')+str(d200)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "c", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dbolu , (str('Upper Bolinger: ')+str(dbolu)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dbolm , (str('Middle Bolinger: ')+str(dbolm)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dboll , (str('Lower Bolinger: ')+str(dboll)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dclose , (str('Close: ')+str(dclose)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "k", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="white", rotation=rtr)






#define width of candlestick elements
width = 0.9
width2 = .08

#define up and down prices
up = aa[aa.Close>=aa.Open]
down = aa[aa.Close<aa.Open]

#define colors to use
col1 = '#03FF29'
col2 = '#FF033E'


aa[['200MA']].plot(ax=ax1,legend=True, linestyle='solid', color='c', linewidth= 1) #Remove legend and on primary axis
#aa[['High']].plot(ax=ax1,legend=False, linestyle='dashed', color='g', linewidth= 1)
#aa[['Low']].plot(ax=ax1,legend=False, linestyle='dashed', color='r', linewidth= 1)
aa[['50MA']].plot(ax=ax1,legend=True, linestyle='solid', color='m', linewidth= 1)
#aa[['EMA50']].plot(ax=ax1,legend=False, linestyle='dotted', color='m', linewidth= 1)
#aa[['Open']].plot(ax=ax,legend=False, color='b', linewidth= .3 )
#aa[['High']].plot(ax=ax,legend=False, color='g', linewidth= .3 )
#aa[['Low']].plot(ax=ax,legend=False, color='r', linewidth= .2 )
aa[['Close']].plot(ax=ax1,legend=True, color='white', linewidth= 0.6 )
#aa[['Volume']].plot(ax=ax4,legend=False, color='k', linewidth= 1.1 )
aa[['30MAM','Bub','Blb']].plot(ax=ax1,legend=False, color='#FF6A00', linestyle='dashed',linewidth= 0.6)
#aa[['52WH','52WL']].plot(ax=ax,legend=False, color='#FF6A00', linestyle='dotted',linewidth= 0.008, alpha = .005)
#aa[['SELL']].plot(ax=ax1,legend=False, color='green', marker ="^", linestyle='solid',linewidth= 4, markersize=5)
#aa[['BUY']].plot(ax=ax1,legend=False, color='red', marker ="o", linestyle='solid',linewidth= 4, markersize=5)

x_axis = aa.index.get_level_values(0)
ax1.fill_between(x_axis, aa['Bub'], aa['Blb'],color='#1F2022', alpha=.4,interpolate=True)









#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)


plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)










plt.xticks(rotation = 0)
ax1.set_title("Nifty Bank Daily Chart", fontsize = 18)
plt.xlabel ('Date')
#ax1.set_xlabel('Theta (radians)')
ax1.set_ylabel('Close Price')
#ax2.set_xlabel('Phi (radians)')



x_axis = aa.index.get_level_values(0)
#print (aa)





#ax1.tick_params(axis="x", direction="in", length=16, width=1, color="turquoise")
#ax1.tick_params(axis="y", direction="in", length=6, width=4, color="orange", labelrotation=90)
#ax1.xaxis.set_minor_locator(AutoMinorLocator(1))
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
#ax1.grid(axis="x", color="green", alpha=.9, linewidth=2, linestyle="solid")
ax1.grid(visible=True, which='major', axis='both')
#ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# set formatter
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))


#plt.title(Title, fontsize = 8)
#plt.show()

plt.savefig("00_DayCandleSrick.png", facecolor=fig.get_facecolor())



################################################################################ ONLY NIFTY add with RSI

fig,(ax1) = plt.subplots(1, sharex=True , sharey=False, constrained_layout=True)
fig.patch.set_facecolor('#4d0026')
fig.set_size_inches(16, 4.5)
ax1.set_facecolor('#4d0026')
plt.xlim(xlim1,xlim2)
plt.ylim(ylim1,ylim2)

ax1.text(Tomm34, d50 , (str('50 Day MA: ')+str(d50)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "m", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, d200 , (str('200 Day MA: ')+str(d200)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "c", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dbolu , (str('Upper Bolinger: ')+str(dbolu)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dbolm , (str('Middle Bolinger: ')+str(dbolm)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dboll , (str('Lower Bolinger: ')+str(dboll)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "#FF6A00", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="k", rotation=rtr)
ax1.text(Tomm34, dclose , (str('Close: ')+str(dclose)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "k", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="white", rotation=rtr)






#define width of candlestick elements
width = 0.9
width2 = .08

#define up and down prices
up = aa[aa.Close>=aa.Open]
down = aa[aa.Close<aa.Open]

#define colors to use
col1 = '#03FF29'
col2 = '#FF033E'


aa[['200MA']].plot(ax=ax1,legend=True, linestyle='solid', color='c', linewidth= 1) #Remove legend and on primary axis
#aa[['High']].plot(ax=ax1,legend=False, linestyle='dashed', color='g', linewidth= 1)
#aa[['Low']].plot(ax=ax1,legend=False, linestyle='dashed', color='r', linewidth= 1)
aa[['50MA']].plot(ax=ax1,legend=True, linestyle='solid', color='m', linewidth= 1)
#aa[['EMA50']].plot(ax=ax1,legend=False, linestyle='dotted', color='m', linewidth= 1)
#aa[['Open']].plot(ax=ax,legend=False, color='b', linewidth= .3 )
#aa[['High']].plot(ax=ax,legend=False, color='g', linewidth= .3 )
#aa[['Low']].plot(ax=ax,legend=False, color='r', linewidth= .2 )
aa[['Close']].plot(ax=ax1,legend=True, color='white', linewidth= 0.6 )
#aa[['Volume']].plot(ax=ax4,legend=False, color='k', linewidth= 1.1 )
aa[['30MAM','Bub','Blb']].plot(ax=ax1,legend=False, color='#FF6A00', linestyle='dashed',linewidth= 0.6)
#aa[['52WH','52WL']].plot(ax=ax,legend=False, color='#FF6A00', linestyle='dotted',linewidth= 0.008, alpha = .005)
#aa[['SELL']].plot(ax=ax1,legend=False, color='green', marker ="^", linestyle='solid',linewidth= 4, markersize=5)
#aa[['BUY']].plot(ax=ax1,legend=False, color='red', marker ="o", linestyle='solid',linewidth= 4, markersize=5)

x_axis = aa.index.get_level_values(0)
ax1.fill_between(x_axis, aa['Bub'], aa['Blb'],color='#1F2022', alpha=.4,interpolate=True)









#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)


plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)










plt.xticks(rotation = 0)
ax1.set_title("Nifty Bank Daily Chart", fontsize = 18)
plt.xlabel ('Date')
#ax1.set_xlabel('Theta (radians)')
ax1.set_ylabel('Close Price')
#ax2.set_xlabel('Phi (radians)')



x_axis = aa.index.get_level_values(0)
#print (aa)





#ax1.tick_params(axis="x", direction="in", length=16, width=1, color="turquoise")
#ax1.tick_params(axis="y", direction="in", length=6, width=4, color="orange", labelrotation=90)
#ax1.xaxis.set_minor_locator(AutoMinorLocator(1))
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
#ax1.grid(axis="x", color="green", alpha=.9, linewidth=2, linestyle="solid")
ax1.grid(visible=True, which='major', axis='both')
#ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# set formatter
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))


#plt.title(Title, fontsize = 8)
#plt.show()

plt.savefig("01_DayCandleSrick_half.png", facecolor=fig.get_facecolor())












########################################################################################################################


fig,(ax2) = plt.subplots(1, sharex=True , sharey=False, constrained_layout=True)
fig.patch.set_facecolor('#4d0026')
fig.set_size_inches(16, 4.5)
ax2.set_facecolor('#4d0026')


plt.xlim(xlim1,xlim2)

aa[['RSI']].plot(ax=ax2,legend=False, linestyle='solid', color='c', linewidth= 2)
#ax2.axhline(0, linestyle='--', alpha=0.1)
#ax2.axhline(20, linestyle='--', alpha=0.5)
ax2.axhline(30, linestyle='solid', color='r', linewidth= .8 )
ax2.axhline(70, linestyle='solid', color='g', linewidth= .8)
ax2.axhline(50, linestyle='dotted', color='k', linewidth= .5)
# ax2.axhline(80, linestyle='--', alpha=0.5)
#ax2.axhline(100, linestyle='--', alpha=0.1)

#ax2.set_xlabel('Phi (radians)')
ax2.set_ylabel('RSI')
ax2.text(Tomm34, drsi , (str('RSI: ')+str(drsi)), bbox=dict(boxstyle = "larrow,pad=0.3",facecolor = "k", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="white", rotation=rtr)


plt.savefig("02_RSI_DayCandleSrick.png", facecolor=fig.get_facecolor())



#######################################################################################################################

fig,(ax3) = plt.subplots(1, sharex=True , sharey=False, constrained_layout=True)
fig.patch.set_facecolor('#4d0026')
fig.set_size_inches(16, 4.5)
ax3.set_facecolor('#4d0026')


plt.xlim(xlim1,xlim2)

x_axis = aa.index.get_level_values(0)
ax3.set_ylabel('MACD')
aa[['Calling']].plot(ax=ax3, legend=False, linestyle='solid', color="#2D38FF", linewidth=1.1)
ax3.axhline(0, color='w', linestyle='solid', linewidth=0.7, alpha=0.5)
ax3.fill_between(x_axis, 0, aa['Calling'], where=(aa['Calling'] <= 0), color='#890000', alpha=1, interpolate=True)
ax3.fill_between(x_axis, 0, aa['Calling'], where=(aa['Calling'] > 0), color='#008933', alpha=1, interpolate=True)
#aa[['Callm']].plot(ax=ax3, legend=False, linestyle='solid', color='c', linewidth=1)
#aa[['Calld']].plot(ax=ax3, legend=False, linestyle='solid', color='c', linewidth=1)
ax3.set_ylabel('MACD')
#ax3.text(Tomm34, drsi , (str('RSI: ')+str(drsi)), bbox=dict(boxstyle = "larrow,pad=0.1",facecolor = "k", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="white")
ax3.text(Tomm34, dmacd0 , (str('MACD - Signal')), bbox=dict(boxstyle = "larrow,pad=0.3",facecolor = "k", edgecolor='#393D47'), fontsize=12, fontweight="bold",horizontalalignment = "left", color ="white", rotation=rtr)


plt.savefig("03_MACD_DayCandleSrick.png", facecolor=fig.get_facecolor())

##################################################################################################################################

































#######################################################################################################################

filnamor = str("SymbolNS")+str('.csv')
dff.to_csv(filnamor)
#plt.show()

filename =  str("SymbolNS")+str('.png')
plt.savefig(filename)

Decri = ["Candle Color", "50 Day Location ", "Bolinger Location", "RSI", "RSI_int","MACD LOC", "MACD DIR", "Todayy", "DayDay"]

tod = datetime.datetime.now()


m3=str (tod.strftime("%B"))
d3=str (tod.strftime("%d"))
today2 = str(d3)+str('  ')+str(m3)





Valus= []
Valus.append(Canle)
Valus.append(day50loc)
Valus.append(BBloc)
Valus.append(drsi)
Valus.append(rsiint)
Valus.append(macdloc)
Valus.append(macddir)
Valus.append(today2)
Valus.append(tod.weekday())





datab = {'Name': Decri, 'Value': Valus}
dVv = pd.DataFrame(datab)
#print (dVv)
dVv.to_csv("00_DailyChartValues.csv")
print ("Daily Chart Data Generated.")
