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


bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'
tod = datetime.datetime.now()
msggg = str('StockMarker Analysis Started') + str('\n') + str(tod)
bot.sendMessage(chat_id, str(msggg))




y3=int (tod.strftime("%Y"))
m3=int (tod.strftime("%m"))
d3=int (tod.strftime("%d"))
h3=int (tod.strftime("%H"))

#print (y3,m3,d3)
today = str(d3)+str('-')+str(m3)+str('-')+str(y3)

dfc = pd.read_csv ('hex.csv')

df = pd.read_csv ('plott.csv')
dl = len(df)
df['width']= 360/dl
df['theta']= "red"
df['colrs']= "red"
df['colrsed']= "red"
XRoff =0.5
YRoff = 0.5
Rrad = 1
df['thetarad'] = 'red'
df['Current'] = 'red'
df['Xr'] = 'red'
df['Yr'] = 'red'
df['rad'] = 'red'
df['theta44'] = 'red'
df['width44'] = 'red'
df['width54'] = 'red'
df['RC'] = 'red'
df['Label'] = 'red'
df['Nrad'] = 'red'
df['PriceN'] = 'red'
Nred = 50
Ngrn = 50

for i in range (0,dl):
    SymbolNS = df['SymbolNS'][i]
    tod = datetime.datetime.now()
    aa = yf.Ticker(SymbolNS)
    aa = aa.history('5y')
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
    aa['Current'] = aa['1D']/aa['Close']
    dll = len(aa)
    dlll = dll -1
    dmmm = dlll -1
    #print (dlll)
    #print (aa['Current'][dlll])
    df['Current'][i] = float((aa['1D'][dlll])/(aa['Close'][dmmm])*100)
    df['PriceN'][i] = aa['Close'][dlll]

    #print(aa)

 


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


    a = buy_sell(aa)
    aa['SELL'] = a[0]
    aa['BUY'] = a[1]



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


    # #print (aa)
dm = dl + 1
df.sort_values(by=['Current'], inplace=True, ascending=False)
df.to_csv("file.csv")

df = pd.read_csv ('file.csv')
for i in range (0,dl):
    df['rad'][i]= abs(df['Current'][i])


dl = len(df)
norm = float (df['rad'].max())
df['Nrad']= df['rad']/norm

REDS = 0
GREENS = 0

for i in range (0,dl):

    RC = (df['Nrad'][i])
    RRRad = ((RC)/1.88)+.023
    df['RC'][i]=RC
    if RC < 0.4:
        RRRad = .22
    sect = 360/dl
    df['theta'][i] = (sect * i)
    df['theta44'][i] = df['theta'][i]  *3.14/180
    df['width44'][i] = sect * i *3.14/180
    df['width54'][i] = sect * 3.14 / 180
    tt = sect * i
    ttt = tt*3.14/180
    #print ("ttt",i, tt, ttt, math.cos(ttt), math.sin(ttt), XRoff, Rrad, YRoff)



    #df['theta44'][i] =df['theta'][i]*3.14/180
    #df['width44'][i] =df['width'][i]*3.14/180

    df['Xr'][i] = XRoff + (RRRad * math.cos(ttt))
    df['Yr'][i] = YRoff + (RRRad * math.sin(ttt))
    #print (df['Xr'][i],df['Yr'][i] )



    cc = df['Current'][i]
    if cc>0 or cc==0:
        df['colrs'][i] = "#013220"
        df['colrsed'][i] = dfc['GRN'][Ngrn]
        Ngrn = Ngrn - 1
        GREENS = GREENS + 1


    if cc<0 :
        df['colrs'][i] = "#45011a"
        df['colrsed'][i] = dfc['RED'][Nred]
        Nred = Nred - 1
        REDS = REDS + 1

    #print (df['colrs'][i])
    #print (i)
    Curry = round((df['Current'][i]),2)
    df['Label'][i] = str(df['Symbol'][i])+str(" (")+ str(Curry)+str("%)")

df.to_csv("file2.csv")



df = pd.read_csv ('file2.csv')

dl = len(df)

plt.style.use('fivethirtyeight')
fig, (ax1) = plt.subplots(1, sharex=True)
fig.set_size_inches(48, 24)
plt.rcParams["font.weight"] = "bold"
theta = df['theta44']
radii = df['Nrad']
width = df['width54']
colors =df['colrsed']

ax = plt.subplot(projection='polar')
#ax = plt.subplot()
fig.patch.set_facecolor('#120052')
ax.set_facecolor('#120052')



ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=1,linewidth=0 , edgecolor='b')

#print (df)

for i in range (0,dl):
    thea = ((df['theta'][i]))


    


    if thea <=90 and thea>=0:
        ax.text(df['Xr'][i], df['Yr'][i], df['Label'][i], transform=ax.transAxes, fontsize=12, color=df['colrsed'][i], alpha=0.9,ha='center', va='center', rotation=(thea+180))

    if thea <=180 and thea>90:
        ax.text(df['Xr'][i], df['Yr'][i], df['Label'][i], transform=ax.transAxes, fontsize=12, color=df['colrsed'][i], alpha=0.9,ha='center', va='center', rotation=(thea+180))

    if thea <=270 and thea>180:
        ax.text(df['Xr'][i], df['Yr'][i], df['Label'][i], transform=ax.transAxes, fontsize=12, color=df['colrsed'][i], alpha=0.9,ha='center', va='center', rotation=(thea+180))

    if thea <=360 and thea>270:
        ax.text(df['Xr'][i], df['Yr'][i], df['Label'][i], transform=ax.transAxes, fontsize=12, color=df['colrsed'][i], alpha=0.9,ha='center', va='center', rotation=(thea+180))


####################### Nifty

SymbolNS = "^NSEI"
aa = yf.Ticker(SymbolNS)
aa = aa.history('5y')
aa['1D'] = aa.Close.diff()
aa['Current'] = aa['1D']/aa['Close']
dll = len(aa)
dlll = dll -1
dmmm = dlll -1
NSEP = round ((float((aa['1D'][dlll])/(aa['Close'][dmmm])*100)),2)
NSEC = round ((aa['Close'][dlll]),2)



plt.style.use('cyberpunk')
fig.set_size_inches(16, 9)
fig.patch.set_facecolor('#120052')
plt.tight_layout()
plt.axis('off')
#plt.show()
plt.savefig('POLAR.png',transparent=False, facecolor='#120052')

plt.close("all")
plt.close()

plt.clf()


#############################################################################

df = pd.read_csv ('file2.csv')

NameS =[]
Symbi = []
Perc =[]
XX = []
YY = []
COLSD =[]

xxg = 90
yy = 250
xxl = 1130
ydl = 125

dfG = df.head(5)
dfL = df.tail(5)
print (dfL)
#print (dfL)
for i in range (0,len(dfG)):
    if dfG['Current'][i]>0:
        NameS.append (dfG['Company Name'][i])
        Symbi.append(dfG['Symbol'][i])
        Perc.append(round(dfG['Current'][i],2))
        XX.append(xxg)
        YY.append(yy)
        xxg = xxg
        yy = yy + ydl

        cols = "#e6ffe6"
        COLSD.append(cols)



    if dfG['Current'][i]<=0:
        NameS.append ("Error")
        Symbi.append("Error")
        Perc.append("0")
        XX.append(xxg)
        YY.append(yy)
        xxg = xxg + 5000
        yy = yy + ydl
        cols = "#e6ffe6"
        COLSD.append(cols)


yy = 750

for i in range(45, 50):
    if dfL['Current'][i] < 0:
        NameS.append(dfL['Company Name'][i])
        Symbi.append(dfL['Symbol'][i])
        Perc.append(round(dfL['Current'][i], 2))
        XX.append(xxl)
        YY.append(yy)
        xxl = xxl
        yy = yy - ydl
        cols = "#ffe6e6"
        COLSD.append(cols)

    if dfL['Current'][i] >= 0:
        NameS.append("Error")
        Symbi.append("Error")
        Perc.append("0")
        XX.append(xxg)
        YY.append(yy)
        xxl = xxl
        yy = yy - ydl
        cols = "#ffe6e6"
        COLSD.append(cols)

datab = {'Name': NameS, 'Symbol': Symbi, 'Perc': Perc, "X": XX, "Y": YY, "COLS": COLSD, "GreenS": GREENS, "Reds":  REDS}
dGL = pd.DataFrame(datab)
dGL.to_csv("00_GainLose.csv")

#######################################IMAGE

Image1 = Image.open('POLAR.png').convert('RGBA')

# make a copy the image so that
# the original image does not get affected
Image1copy = Image1.copy()
text = str('Nifty50') + str('\n') +str(NSEC) + str('\n') + str(NSEP) + str("%") + str('\n') + str(today)
siz = 45
font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (300, 50))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (250, 100), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "white")
px, py = 10, 10
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)


Image1copy = Image1.copy()
text = str('Nifty 50 : Top Gainers and Top Losers' )

font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (1920, 1080))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "white")
px, py = 350, 10
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)

#######################################

siz = 40

##################################### Gainers


text = str('Top Gainers' )
font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (1920, 1080))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "#26FE0C")
px, py = 80, 125
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)




##################################### Losers


text = str('Top Losers' )
font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (1920, 1080))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "#FB1E0F")
px, py = 1130, 125
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)


###############################################


##################################### GREEN


text = str('Greens = ' ) +  str(int(dGL["GreenS"][0]))
font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (1920, 1080))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "#26FE0C")
px, py = 88, 15
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)


text = str('Reds = ' ) +  str(int(dGL["Reds"][0]))
font = ImageFont.truetype('Bold.ttf', size=siz)
text_layer = Image.new('L', (1920, 1080))
draw = ImageDraw.Draw(text_layer)
image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(image2)
draw2.text((15, -5), text=text, font=font, fill= "#FB1E0F")
px, py = 1270, 15
sx, sy = image2.size
Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)













##################################### Stks

siz = 30



dll = len (dGL)
for i in range (0, dll):
    if dGL["Name"][i] != "Error":
        try:
            text = str(dGL["Symbol"][i]) + str(" : ") + str(round (dGL["Perc"][i],1))+ str(" %")
            font = ImageFont.truetype('Bold.ttf', size=siz)
            text_layer = Image.new('L', (1920, 1080))
            draw = ImageDraw.Draw(text_layer)
            image2 = PIL.Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
            draw2 = ImageDraw.Draw(image2)
            draw2.text((15, -5), text=text, font=font, fill= dGL["COLS"][i])
            px, py = dGL["X"][i], dGL["Y"][i]
            sx, sy = image2.size
            Image1copy.paste(image2, (px, py, px + sx, py + sy), image2)
        except:
            print ("ERRRRRRRRROR")

Image1copy.save("06_TopGailLose.png", quality=100)

print ("Gain Loss Data Generated.")