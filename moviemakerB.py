
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
import moviepy.editor as mp
from moviepy.editor import *

#####################################################################

clips=[]

df = pd.read_csv ('videolistB.csv')
dll = len (df)
print (df)
for i in range (0, dll):
    print ("Started: ", str(df["mpss"][i]))
    AUDIOFF= str(df["mpss"][i]) + str(".mp3")
    PICCC = str(df["imagesss"][i]) + str(".png")
    VIDEOO = str(df["mpss"][i]) + str(".mp4")

    audioclip = AudioFileClip(AUDIOFF)
    timy= audioclip.duration
    print (timy)
    clip001 = ImageClip(PICCC).set_duration(timy)
    clip001r = clip001.resize ((1920,1080))
    clip001r2 = clip001r.set_audio(audioclip)
    clips.append(clip001r2)
    video_clip = concatenate_videoclips(clips, method = 'compose')



# Apply speed up
video_clip = video_clip.fx(vfx.speedx, 1.1)

print("fps: {}".format(video_clip.fps))

video_clip.write_videofile("000_Upload_This.mp4", fps=25, codec="libx264", remove_temp=True, audio_codec="aac", threads=32)


print ("movie made")
'''

##################################################################### APPPEND ALLL!!!!!!!

clips.append(clip001r2)
clips.append(clip002r2)
clips.append(clip003r2)
clips.append(clip004r2)
clips.append(clip005r2)
clips.append(clip006r2)
clips.append(clip007r2)
clips.append(clip008r2)
clips.append(clip009r2)
clips.append(clip010r2)
clips.append(clip011r2)
clips.append(clip012r2)
'''



