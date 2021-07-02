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
f = open('C:\\Users\\Shane\\proj\\Google Maps\\Takeout\All\\2016_NOVEMBER.json')
data = json.load(f)
p=open('C:\\Users\\Shane\\proj\\Google Maps\\CSV_1','w')

Counties = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']

# CREATE THE CSV FILE from json file
count=0
for i in data['timelineObjects']:
    #lat = data['timelineObjects'][count].keys()
    key1='activitySegment'
    if(key1 in data['timelineObjects'][count]):
        lat = str(data['timelineObjects'][count]['activitySegment']['endLocation']['latitudeE7'])
        longi = str(data['timelineObjects'][count]['activitySegment']['endLocation']['longitudeE7'])
        print(str(count)+ ' '+'Latitude = '+lat+' ' + 'Longitude = '+longi)
        row = [str(count),str(lat),str(longi)]
        p.writelines(row)
    else : 
        adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
        for i in Counties:
            if (i in adr):
                print(i)
                adr = adr.replace("\n", "\t")
                adr = adr.strip()
                print(str(count)+ ' '+adr)
                row2=[str(count),adr]
                p.writelines(row2)
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

f.close()