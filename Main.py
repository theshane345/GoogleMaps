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
import datetime as dt
import time
from datetime import datetime
f = open('C:\\Users\\Shane\\proj\\Google Maps\\Takeout\All\\2019_NOVEMBER.json')
data = json.load(f)
p=open('C:\\Users\\Shane\\proj\\Google Maps\\CSV_1.csv','w')

Counties = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']


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
        end = data['timelineObjects'][count]['placeVisit']['duration']['endTimestampMs']

        con = str(data['timelineObjects'][count]['placeVisit']['placeConfidence'])
        start = data['timelineObjects'][count]['placeVisit']['duration']['startTimestampMs']
        for i in Counties:
            if (i in adr):
                adr = adr.replace("\n", "\t")
                adr = adr.strip()
                print(str(count)+ ' '+adr)
                endi=int(end)
                rend = datetime.fromtimestamp(endi).strftime('%Y-%m-%d %H:%M:%S')
                rstart = datetime.datetime.fromtimestamp(float(start)/1000.)
                date = date.datetime.fromtimestamp(float(start)/1000.).strftime('%Y-%m-%d')
                d['Address']=adr
                d['County']=i
                d['Name']=name
                d['Start time']=rstart
                d['End time']=rend
                d['Date'] = date
                d['Location confidence']=con
                rows.append(d)
                dfGoogleStats = pd.DataFrame(rows)
                today = date.today()
                d1 = today.strftime("%d_%m_%Y")
                dfGoogleStats.to_csv(f'C:\\Users\\Shane\\proj\\Google Maps\\GoogleMaps_{d1}.csv', index=False)
    count=count+1

#data = dict(type = 'choropleth',
            #locations = ['Ireland'],
            #locationmode = 'country names',
            #colorscale= 'Portland',
            #text= ['text1'],
            #z=[1.0],
            #colorbar = {'title':'Colorbar Title'})

#layout = dict(geo = {'scope':'Ireland'})
#choromap = go.Figure(data = [data],layout = layout)
#iplot(choromap)

#count2 = 1
#for i in data['timelineObjects'][count]:
   # count2= +2AAA
    #adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
    

   # print('location = '+adr)
p.close()
f.close()