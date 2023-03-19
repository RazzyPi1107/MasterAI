
from instabot import Bot
import time
import schedule
import datetime
from datetime import date, timedelta
import telepot
from telepot.loop import MessageLoop
import sys
import os
import random
from os import listdir
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
#from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop
from time import strftime
import telepot
from telepot.loop import MessageLoop
import time
#import mplcyberpunk
from matplotlib.gridspec import GridSpec
import matplotlib.dates as mdates
from nsepython import *
import matplotlib.pyplot as plt
import numpy as np
import os

t = 9
while t<10:
    bb = nse_fiidii()
    print("--------------------------------------------------------------")

    print (bb)
    ############### Random Delay
    a2 = datetime.datetime.now()
    y3=int (a2.strftime("%Y"))
    m3=str (a2.strftime("%b"))
    d3=int (a2.strftime("%d"))
    h3=int (a2.strftime("%H"))
    M3 = int(a2.strftime("%M"))
    if d3<10:
        d3 = (str(d3).rjust(2, '0'))
    today = str(d3)+str('-')+str(m3)+str('-')+str(y3)
    tyme = str(h3)+str(':')+str(M3)

    print ("--------------------------------------------------------------")
    print (today)

    FIDate = str(bb['date'][0])

    print(FIDate)
    print("--------------------------------------------------------------")
    print(tyme)
    print("--------------------------------------------------------------")
    #time.sleep(360)

    if FIDate == today:
        t =1000
        print ("IIIIINNNNNN")




        msgk = str("DataUpdated") + str("\n") + str(bb)

        ############### Telegram Bot Setup

        bbot = telepot.Bot('5226423541:AAHQ4s7Pl-COf6-5-nBOMk7oJM3dax1SW8U')
        chat_id = '1047135684'
        bbot.sendMessage(chat_id, str(msgk))


        #bot.sendPhoto(chat_id, photo=open(filename, 'rb'), caption = captain)


        a2 = datetime.datetime.now()
        bbot = telepot.Bot('5226423541:AAHQ4s7Pl-COf6-5-nBOMk7oJM3dax1SW8U')
        chat_id = '1047135684'

        msgk = str("MasterAI Started:") + str("\n") + str(a2)
        bbot.sendMessage(chat_id, str(msgk))

        import IntraDate
        import IntraNifty
        import Nifty_Pivot
        import polarbar
        import optioncall
        import optionput
        import fiii
        import RSIChart
        import MACDChart
        import titlepage_gen
        import scriptss
        import reader_01
        import moviemaker
        import Video_Tilte

        print ('''
        
        
                                                                               xmHTTTTT%ms.
                                                                            z?!!!!!!!!!!!!!!?m
                                                                          z!!!!!!!!!!!!!!!!!!!!%
                                                                       eHT!!!!!!!!!!!!!!!!!!!!!!!L
                                                                      M!!!!!!!!!!!!!!!!!!!!!!!!!!!>
                                                                   z!!!!!!!!!!XH!!!!!!!!!!!!!!!!!!X
                                                                   "$$F*tX!!W?!!!!!!!!!!!!!!!!!!!!!
                                                                   >     M!!!   4$$NX!!!!!!!!!!!!!t
                                                                   tmem?!!!!?    ""   "X!!!!!!!!!!F
                                                              um@T!!!!!!!!!!!!s.      M!!!!!!!!!!F
                                                           .#!!!!!!!!!!!!!!!XX!!!!?mM!!!!!!!!!!t~
                                                          M!!!@!!!!X!!!!!!!!!!*U!!!!!!!!!!!!!!@
                                                         M!!t%!!!W?!!!XX!!!!!!!!!!!!!!!!!!!!X"
                                                        :!!t?!!!@!!!!W?!!!!XWWUX!!!!!!!!!!!t
                                                        4!!$!!!M!!!!8!!!!!@$$$$$$NX!!!!!!!!-
                                                         *P*!!!$!!!!E!!!!9$$$$$$$$%!!!!!!!K
                                                            "H*"X!!X&!!!!RR$$$*#!!!!!!!!!>
                                                                'TT!?W!!9!!!!!!!!!!!!!!!!M
                                                                '!!!!!!!!!!!!!!!!!!!!!!!!F
                                                                '!!!!!!!!!!!!!!!!!!!!!!!!>
                                                                '!!!!!!!!!!!!!!!!!!!!!!!M
                                                                J!!!!!!!!!!!!!!!!!!!!!!!F K!%n.
                 @!!!!!??m.                                  x?F'X!!!!!!!!!!!!!!!!!!!!HP X!!!!!!?m.
        Z?L      '%!!!!!!!!!?s                            .@!\~ MB!!!!!!!!!!!!!!!!!U#!F X!!!!!!!!X#!%.
        E!!N!k     't!!!!!!!!!?:                       zTX?!t~ M!t!!!!!!!!!!!!!!UM!!!F 4!!!!!!!!t%!!!!?.
        !!!!!!hzh.   "X!!!!!!!!!>                  .+?!!3?!X  Z!!!B!!!!!!!!!!UM!!!!!" 4!!!!!!!!t?!!!!!!!h
        ?!!!!!!!!!*!?L %!!!!!!!!?               .+?!!!!3!!\  P!!!!?X!!!!!!U#!!!!!!X" 4!!!!!!!!\%!!!!!!!!!?
        'X!!!!!!!!!!!!?TTTT*U!!!!k            z?!!!!!!t!!!- J!!!!!!9!!X@T!!!!!!!!X~ d!!!!!!!!!%!!!!!!!!!!!!L
         4!!!!!!!!!!!!!!!!!!!!!!!M          'W!!!!!!!X%!!P  %!!!!!!!T!!!!!!!!!!!X~ J!!!!!!!!!P!!!!!!!!!!!!!!l
          5!!!!!!!!!!!!!!!!!!!!!!!?m.       .@Ti!!!!!Z!!t  d!!!!!!!!!!!!!!!!!!!X-.JUUUUX!!!!J!!!!!!!!!!!!!!!!!
           %!!!!!!!!!!!!!!!!!!!!!!!!!!!TnzT!!!!!#/!!?!!X"  ^"=4UU!!!!!!!!!!U@T!!!!!!!!!!!!Th2!!!!!!!!!!!!!!!!!!
            ^t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?K!K!!f               `""#X!!!!!!!!!!!!!!!!!?t!!!!!!!!!!!!!!!!(>
               "U!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!$!!F                      "tX!!!!!!!!!!!!!!!!b!!!!!!!!!!!!!!!(>
                  '"*tUUX!X!!!!!!!!!!!!!!!!!!!!!!!!$!Z                          ^4!!!!!!!!!!!!!!!N!!!!!!!!!!!!!!!!
                         %!!!!!!!!!!!!!!!!!!!!!!!!X!X                              %W@@WX!!!!!!!!!N!!!!!!!!!!!!!!!
                          "X!!!!!!!!!!!!!!!!!!!!!@!!*        ..    ..  :m.. ETThmuM!!!!!!!!!!!!!!!!@m@*TTTT?!!!W!!
                            %!!!!!!!!!!!!!!!!!!W?!!X         M!!!TT?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!9UU!!!!!!!!!M!f
                             't!!!!!!!!!!!!!!!P!!!!X          5!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?NX!!!!!!L
                               "W!!!!!!!!!!!X#!!!!!R           "X!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!R!!!!!t
                                 ^*X!!!!!!!t%!!!!!h              %X!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>
                                     "*U!!M!!!!!!X~ :?!!!T!+s...   *X!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                         :?!!!!!!> :?!!!!!!!!!!!!!!!!?tX!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>
                                         %!!!!!!F .%!!!!!!!!!!!!!!!!!!!!!#4U!!!!!!!!!!!!U!!!!!!!!!!!!!!!!!!!!!!!!~
                                        K!!!!!!Z  K!!!!!!!!!!!!!!!!!!!!!!!  F!!!!!?!!?X!!!!!!!!!!!!!!!!!!!!!!!!!Z
                                       X!!!!!!t  H!!!!!!!!!!!!!!!!!!!!!!!!> !!!!!!!!!!!W!!!!!!!!!!!!!!!!!!!!!!!t
                                       %!!!!!!F :!!!!!!!!!!!!!!!!!!!!!!!!!> !!!!!!!!!!!!#X!!!!!!!!!!!!!!!!!!!!X
                                      '!!!!!!X  K!!!!!!!!!!!!!!!!!!!!!!!!!> K!!!!!!!!!!!!!?W!!!!!!!!!!!!!!!!X"
        
        ''')


        a2 = datetime.datetime.now()
        msgk = str("MasterAI Ended:") + str("\n") + str(a2)
        bbot.sendMessage(chat_id, str(msgk))
        df2 = pd.read_excel('0000_Final_Final_Title.xlsx')
        TITLESS = str((df2['Heading'][0]))  + str((df2['Heading'][1])) + str(" | ") + str((df2['Heading'][2]))
        bbot.sendMessage(chat_id, str(TITLESS))
        filenameP = str(r'C:\01_PythonCodes\Gr8\MasterAI\UPLOAD\0000000000_TITILE.png')
        filenameV = str(r'C:\01_PythonCodes\Gr8\MasterAI\UPLOAD\000_Upload_This.mp4')
        bbot.sendPhoto(chat_id, photo=open(filenameP, 'rb'), caption = TITLESS)
        #bbot.sendVideo(chat_id, video=open(filenameV, 'rb'), caption = TITLESS)

    time.sleep(360)