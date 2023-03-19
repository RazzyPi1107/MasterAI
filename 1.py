
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


SymbolNS ='SBILIFE.NS'

aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com

aa = aa.history('3y')

print (aa)