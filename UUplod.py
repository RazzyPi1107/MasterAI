import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import pandas as pd
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
import shutil, os

df2 = pd.read_excel('0000_Final_Final_Title.xlsx')
TITLESS = str("2 Min |") + str((df2['Heading'][0]))  + str((df2['Heading'][1]))

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#upload_date_time = datetime.datetime(2022, 4, 14, 13, 59, 0).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': TITLESS,
        'description': 'I am Gr8. I strongly believe that but also I believe that you and everyone is gr8. Everyone has G8ness in them that needs to be shared. Knowledge is power. And we must learn to remain The Gr8. I am not a SEBI registered adviser. All the information provided here are for educational/informational purposes only. I will not be responsible for any of your profit/loss with this suggestions. Consult your financial advisor before taking any decisions. Information here are neither advice nor endorsement.',
        'tags': ['Sharemarket', 'Automation', 'Python']
    },
    'status': {
        'privacyStatus': 'public',
        #'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': True
}

mediaFile = MediaFileUpload('000_Upload_This.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()


service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('0000000000_TITILE.png')
).execute()