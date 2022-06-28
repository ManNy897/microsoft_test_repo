import json
import csv 

import xml.etree.ElementTree as ET
from lxml import etree

import pandas as pd
from pandasql import sqldf



f = open('/Users/manny/Downloads/hawker-centres/hawker-centres-geojson.geojson')
data = json.load(f)
hawker_centres = {}
hawker_centers_list = []
for feature in data['features']:
	try:
		longitude = feature["geometry"]["coordinates"][0]
		latitude = feature["geometry"]["coordinates"][1]
		xml = feature["properties"]["Description"]
		root = etree.fromstring(xml)
		name = root.xpath('.//table/tr/th[text()="NAME"]/../td')[0].text
		photo_url = root.xpath('.//table/tr/th[text()="PHOTOURL"]/../td')[0].text
		hawker_centres[name] = {"photo_url":photo_url, "latitude":latitude, "longitude":longitude}
		hawker_centers_list.append([name, photo_url, longitude, latitude])
	except:
		print("failed to get photo url")
		print("xlm: " + str(xml))
		continue;
	# print(len(hawker_centres))
	# hawker_centres.append({"name":name, "photo_url":photo_url, "latitude":latitude, "longitude":longitude})
f.close()

json_dataset = json.dumps(hawker_centres, indent = 4)
with open("json_dataset.json", "w") as outfile:
	outfile.write(json_dataset)

fields = ['Name', 'Photo_Url', 'Longitude', 'Latitude'] 
with open("csv_dataset.csv", "w") as outfile:
	csvwriter = csv.writer(outfile) 
	csvwriter.writerow(fields)
	csvwriter.writerows(hawker_centers_list)

df = pd.DataFrame(hawker_centers_list, columns=fields) 
# print(df.head())
query = """SELECT Name, ( 3959 * acos( cos( radians(37) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians(-122) ) + sin( radians(37) ) * sin( radians( lat ) ) ) ) AS distance FROM df HAVING distance < 25 ORDER BY distance LIMIT 0 , 20"""
output = sqldf(query)
# output = sqldf("select * from df where Name ='Marine Terrace Blk 50A (50A Marine Terrace)'")
print(output)


# print(df.head())

