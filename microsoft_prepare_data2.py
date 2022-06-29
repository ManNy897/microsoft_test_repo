import json
import csv
import re

# import xml.etree.ElementTree as ET
# from lxml import etree

#############################################################
#####function to extract name and photo url from xml string using regex

name_regex = '<th>NAME</th> <td>(.*?)</td>'
photo_regex = '<th>PHOTOURL</th> <td>(.*?)</td>'

def get_name_and_photo_url(xml_string):
	name_regex_result = re.search(name_regex, xml)
	name = None
	if name_regex_result != None:
		name = name_regex_result.group(1)
	else:
		print("no name")


	photo_regex_result = re.search(photo_regex, xml)
	photo_url = None
	if photo_regex_result != None:
		photo_url = photo_regex_result.group(1)
	else:
		print("no photo")
	return name, photo_url

################################
###function to update max and min values

minLat = float('inf')
maxLat = float('-inf')
minLon = float('inf')
maxLon = float('-inf')
def update_min_max_values(latitude, longitude):
	global minLat
	global maxLat
	global minLon
	global maxLon

	if latitude < minLat:
		minLat = latitude
	if latitude > maxLat:
		maxLat = latitude
	if longitude < minLon:
		minLon = longitude
	if longitude > maxLon:
		maxLon = longitude



###############################
##############read the file####
with open("hawker-centres-geojson.geojson", "r") as inputfile:
	data = json.load(inputfile)

hawker_centres = {}
hawker_centers_list = []

for feature in data['features']:
	longitude = feature["geometry"]["coordinates"][0]
	latitude = feature["geometry"]["coordinates"][1]
	update_min_max_values(latitude, longitude)
	xml = feature["properties"]["Description"]

	name, photo_url = get_name_and_photo_url(xml)

	# print(xml)
	# root = etree.fromstring(xml)
	# name = root.xpath('.//table/tr/th[text()="NAME"]/../td')[0].text
	# photo_url = root.xpath('.//table/tr/th[text()="PHOTOURL"]/../td')[0].text
	hawker_centres[name] = {"photo_url":photo_url, "latitude":latitude, "longitude":longitude}
	hawker_centers_list.append([name, photo_url, longitude, latitude])

print(len(hawker_centres))
print(minLon)
print(maxLon)
print(minLat)
print(maxLat)

###################################
#######split the data in fourthes##
halfLon = ((maxLon - minLon)/2.0) + minLon
halfLat = ((maxLat - minLat)/2.0) + minLat
print(halfLon)
print(halfLat)

hawker_centres_1 = {}
hawker_centres_2 = {}
hawker_centres_3 = {}
hawker_centres_4 = {}
for key in hawker_centres:
	if(hawker_centres[key]["latitude"] <= halfLat and hawker_centres[key]["longitude"] >= halfLon):
		hawker_centres_1[key] = hawker_centres[key]
	elif(hawker_centres[key]["latitude"] > halfLat and hawker_centres[key]["longitude"] >= halfLon):
		hawker_centres_2[key] = hawker_centres[key]
	elif(hawker_centres[key]["latitude"] > halfLat and hawker_centres[key]["longitude"] < halfLon):
		hawker_centres_3[key] = hawker_centres[key]
	else:
		hawker_centres_4[key] = hawker_centres[key]

print(len(hawker_centres_1))
print(len(hawker_centres_2))
print(len(hawker_centres_3))
print(len(hawker_centres_4))
#######################################
############write out the datasets#####
datasets = [hawker_centres_1, hawker_centres_2, hawker_centres_3, hawker_centres_4]
for i in range(4):
	json_dataset = json.dumps(datasets[i], indent = 4)
	with open("json_dataset"+str(i+1)+".json", "w") as outfile:
		outfile.write(json_dataset)


