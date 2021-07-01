import pandas as pd
import json

f = open('C:\\Users\\Shane\\proj\\Google Maps\\Takeout\All\\2016_NOVEMBER.json')
data = json.load(f)



count=0
for i in data['timelineObjects']:
    #lat = data['timelineObjects'][count].keys()
    key1='activitySegment'
    if(key1 in data['timelineObjects'][count]):
        lat = str(data['timelineObjects'][count]['activitySegment']['endLocation']['latitudeE7'])
        longi = str(data['timelineObjects'][count]['activitySegment']['endLocation']['longitudeE7'])
        print(str(count)+ ' '+'Latitude = '+lat+' ' + 'Longitude = '+longi)
        
    else : 
        adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
        adr = adr.replace("\n", "\t")
        adr = adr.strip()
        print(str(count)+ ' '+adr)

    count=count+1



#count2 = 1
#for i in data['timelineObjects'][count]:
   # count2= +2
    #adr = str(data['timelineObjects'][count]['placeVisit']['location']['address'])
    

   # print('location = '+adr)

f.close()