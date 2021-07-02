import pandas as pd
import json
import numpy as np
import cufflinks as cf
import matplotlib.pyplot as plt
import seaborn as sns
import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import datetime 
from datetime import datetime
import time

cf.go_offline()

fig=go.Figure()

f = open('C:\\Users\\Shane\\proj\\Google Maps\\Takeout\All\\2019_NOVEMBER.json')
data = json.load(f)
p=open('C:\\Users\\Shane\\proj\\Google Maps\\CSV_1.csv','w')

Counties = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']
today = datetime.today()
d1 = today.strftime("%d_%m_%Y")

rows=[]
d={}
# CREATE THE CSV FILE from json file
count=0
for i in data['timelineObjects']:
    #lat = data['timelineObjects'][count].keys()
    key1='activitySegment'
    if(key1 in data['timelineObjects'][count]):
        atype = str(data['timelineObjects'][count]['activitySegment']['activityType'])
        lat = str(data['timelineObjects'][count]['activitySegment']['endLocation']['latitudeE7'])
        accon= str(data['timelineObjects'][count]['activitySegment']['confidence'])
        longi = str(data['timelineObjects'][count]['activitySegment']['endLocation']['longitudeE7'])
        print(str(count)+ ' '+'Latitude = '+lat+' ' + 'Longitude = '+longi)
        #row = [str(count),str(lat),str(longi)]
        d={}
        d['Activity Type']=atype
        d['Activity Confidence']=accon
        d['Latitude']=lat
        d['Longitude']=longi
        
       
    else : 
        adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
        name = str(data['timelineObjects'][count]['placeVisit']['location']['name'])
        end = str(data['timelineObjects'][count]['placeVisit']['duration']['endTimestampMs'])

        con = str(data['timelineObjects'][count]['placeVisit']['placeConfidence'])
        start = str(data['timelineObjects'][count]['placeVisit']['duration']['startTimestampMs'])
        for i in Counties:
            if (i in adr):
                adr = adr.replace("\n", "\t")
                print(str(count)+ ' '+adr) 
                rend = datetime.fromtimestamp(int(end)/1000).strftime('%Y-%m-%d %H:%M:%S')
                rstart = datetime.fromtimestamp(int(start)/1000).strftime('%Y-%m-%d %H:%M:%S')
                date = datetime.fromtimestamp(float(start)/1000).strftime('%Y-%m-%d')
                d['Address']=adr
                d['County']=i
                d['Name']=name
                d['Start time']=rstart
                d['End time']=rend
                d['Date'] = date
                d['Location confidence']=con
                rows.append(d)
                dfGoogleStats = pd.DataFrame(rows)
                
                dfGoogleStats.to_csv(f'C:\\Users\\Shane\\proj\\Google Maps\\GoogleMaps_{d1}.csv', index=False)
    count=count+1


#CREATE CHARTS BASED OFF OF DATA
#DISTPLOT
df=pd.read_csv(f'C:\\Users\\Shane\\proj\\Google Maps\\GoogleMaps_{d1}.csv')
data = df['County'].iplot(kind='hist')


choromap = go.Figure(data = [data])
iplot(choromap)

#count2 = 1
#for i in data['timelineObjects'][count]:
   # count2= +2AAA
    #adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
    

   # print('location = '+adr)
p.close()
f.close()