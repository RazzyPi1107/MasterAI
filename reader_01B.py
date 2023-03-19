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


df1 = pd.read_excel('0000_Final_Read_script.xlsx')


##################################################################### Intro
scripty = " "
start = 0
end = 1
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("001_Intro.mp3")

##################################################################### Disclaimer
scripty = " "
start = 1
end = 2
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("002_Disclaimer.mp3")

##################################################################### IntraDay
scripty = " "
start = 2
end = 32
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("003_IntraDay.mp3")

##################################################################### DailyChartFull
scripty = " "
start = 32
end = 40
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("004_DailyChart_Full.mp3")

##################################################################### DailyChartRSI
scripty = " "
start = 40
end = 45
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("005_DailyChart_RSI.mp3")

##################################################################### DailyChartMACD
scripty = " "
start = 45
end = 51
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("006_DailyChart_MACD.mp3")

'''
##################################################################### TopGainLoss
scripty = " "
start = 51
end = 77
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("007_TopGainLoss.mp3")
'''
##################################################################### FiiDii
scripty = " "
start = 77
end = 95
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("008_FiiDii.mp3")

##################################################################### OptionChainCALL
scripty = " "
start = 95
end = 103
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("009_OptionChainCALL.mp3")

##################################################################### OptionChainPUT
scripty = " "
start = 103
end = 115
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("009_OptionChainPUT.mp3")


##################################################################### PivotPoints
scripty = " "
start = 115
end = 127
for i in range (start,end):
    scripty = scripty + str(" ") + str(df1['thisssayer'][i])
    print (scripty)
tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("010_PivotPoints.mp3")

##################################################################### FinalLikeShare
scripty = " "

scripty = scripty + str(" ") + str(df1['thisssayer'][127])

tts = gtts.gTTS(scripty, lang="mr", tld="co.in")
tts.save("011_FinalLikeShare.mp3")