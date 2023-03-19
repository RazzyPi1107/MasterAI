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
import seaborn as sns
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


plt.style.use('cyberpunk')

SymbolNS ='^NSEI'

aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com

aa = aa.history('3y')
#print (aa)
j1 = aa.shape[0]
jz = j1 - 1

Ntw = aa["Close"][jz]

Tday =[]
Yday=[]
TommD = []
Tomm = datetime.date.today() + datetime.timedelta(days=1)
#print (Tomm)
#print (j1)
j2 = j1 -1
j3 = j1 -2
a2 = aa.index[j2]

a2 = aa.index[j2]


Tomm3 = datetime.date.today() + datetime.timedelta(days=15)
Tomm34 = datetime.date.today() + datetime.timedelta(days=1)

y3=int (a2.strftime("%Y"))
m3=int (a2.strftime("%m"))
d3=int (a2.strftime("%d"))
h3=int (a2.strftime("%H"))

#print (y3,m3,d3)
today = str(y3)+str('-')+str(m3)+str('-')+str(d3)


oi_data, ltp, crontime = oi_chain_builder("NIFTY","latest","full")
#print(oi_data)
#print(ltp)
#print(crontime)

df = oi_data

df.to_csv('nifty.csv')



aa = pd.read_csv("nifty.csv")
vlx = []
df = pd.read_csv("nifty.csv")
df.sort_values(by=['CALLS_OI'], inplace=True, ascending=False)
dff = df.head(3)
dff.to_csv("call.csv")
dft = pd.read_csv("call.csv")
for i in range (1, len(dft)):
    vlx.append(dft['CALLS_OI'][i])


xlim1 = Ntw*0.95
xlim2 = Ntw*1.15

aa.set_index("Strike Price", inplace = True)
dl = len (aa)
#print(aa)

aa['Stk'] = aa.index
data = aa['CALLS_OI']

vminn = aa['CALLS_OI'].min()
vmaxx = aa['CALLS_OI'].max()
vminn1 = aa['CALLS_Chng in OI'].min()
vmaxx1 = aa['CALLS_Chng in OI'].max()



bex1 = aa.index[aa['CALLS_OI']==vmaxx].tolist()
bex2 = aa.index[aa['CALLS_Chng in OI']==vminn1].tolist()
bex3 = aa.index[aa['CALLS_Chng in OI']==vmaxx1].tolist()
bex4 = aa.index[aa['CALLS_OI']==vlx[0]].tolist()
bex5 = aa.index[aa['CALLS_OI']==vlx[1]].tolist()


ListA = []
ListB = []
ListC = []
ListD = []






ListA.append(bex5[0])
ListB.append(vlx[1])
ListC.append(str("3rd Max. CALL OI: ") +str(bex5[0]))
ListD.append("#06038D")

ListA.append(bex4[0])
ListB.append(vlx[0])
ListC.append(str("2nd Max. CALL OI: ") +str(bex4[0]))
ListD.append("#06038D")

ListA.append(bex1[0])
ListB.append(vmaxx)
ListC.append(str("Max. CALL OI: ") +str(bex1[0]))
ListD.append("#06038D")


ListA.append(bex2[0])
ListB.append(vminn1)
ListC.append(str("Max. CALL unwinding: ") +str(bex2[0]))
ListD.append('#651C32')

ListA.append(bex3[0])
ListB.append(vmaxx1)
ListC.append(str("Max. CALL writing: ") +str(bex3[0]))
ListD.append("#154734")



#print("-----------------------------------------------")
#print(bex1)
#print(bex2)
#print(bex3)
#print("-----------------------------------------------")

my_cmap = cm.get_cmap('cool')
# Get normalize function (takes data in range [vmin, vmax] -> [0, 1])
my_norm = Normalize(vmin=vminn, vmax=vmaxx)


fig, ax1 = plt.subplots(constrained_layout=True)



fig.set_size_inches(16, 9)
fig.patch.set_facecolor('#120052')
ax1.set_facecolor('#120052')
aa['CALLS_OI'].plot(ax =ax1, kind='line', color="#0827F5", linestyle='solid',linewidth= .4,)
x_axis = aa.index.get_level_values(0)
ax1.fill_between(x_axis, 0, aa['CALLS_OI'],color="#C710AF", alpha=.99,interpolate=False)


#aa['CALLS_OI'].plot(ax =ax1, kind='line', color=my_cmap(my_norm(data)), linestyle='dashed',linewidth= 4)

#plt.step(aa['Stk'], aa['CALLS_OI'],where='mid', color="red", linestyle='solid',linewidth= 1)

vminn = aa['CALLS_Chng in OI'].min()
vmaxx = aa['CALLS_Chng in OI'].max()
aa['CALLS_Chng in OI'].plot(ax =ax1, kind='line', color="k", linestyle='dotted',linewidth= .4)
ax1.fill_between(x_axis, 0, aa['CALLS_Chng in OI'], where=(aa['CALLS_Chng in OI'] <= 0), color='#FF033E', alpha=.9, interpolate=True)
ax1.fill_between(x_axis, 0, aa['CALLS_Chng in OI'], where=(aa['CALLS_Chng in OI'] > 0), color='#08FF08', alpha=.9, interpolate=True)
my_cmap = cm.get_cmap('RdYlGn')
# Get normalize function (takes data in range [vmin, vmax] -> [0, 1])
my_norm = Normalize(vmin=vminn, vmax=vmaxx)

#aa['CALLS_Chng in OI'].plot(ax= ax1, kind='bar', width = 1, color="red", alpha = 0.8, hatch="x")


Listy = []
Listyx = []


Listy.append (Ntw)
Listyx.append (vmaxx)

for i in range (0,2000, 500):
    kty = Ntw - i
    Listy.append (kty)
    Listyx.append(vmaxx)

for i in range (0,2000, 500):
    kty = Ntw + i
    Listy.append (kty)
    Listyx.append(vmaxx)







ax1.axhline(0, color='#19FF50', linestyle='dotted', linewidth=1, alpha=0.8)




Del = 40

for i in range (0,5):
    ax1.text((ListA[i]+Del), ListB[i], ListC[i], bbox=dict(boxstyle="larrow,pad=0.3", facecolor=ListD[i], edgecolor='yellow'), fontsize=16, fontweight="bold", horizontalalignment="left", color="white", rotation =10)

'''    x = aa['Stk'][i]
    y = aa['CALLS_OI'][i]
    #print (x,y)

'''




#leg = ax1.legend()
ax1.xaxis.set_tick_params(rotation=90)
plt.grid(True)
plt.yticks([])
plt.xlim([xlim1, xlim2])

Titls = str("Nifty Open Intrest CALL  : ") + str(today)


plt.title(Titls, fontsize = 18, loc='left')
#plt.show()



filename =  str("07_Call_Nifty")+str('.png')
plt.savefig(filename, facecolor=fig.get_facecolor())

Decri = ["Candle Color", "50 Day Location ", "Bolinger Location", "RSI", "RSI_int"]






datab = {'Name': ListC, 'Value': ListA}
dfo = pd.DataFrame(datab)
#print (dfo)
dfo.to_csv("00_OptionValuesCall.csv")

print ("CALL Option chain Data Generated.")



