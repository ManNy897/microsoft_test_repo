import json
import csv
import re

name_regex = '<th>NAME</th> <td>(.*?)</td>'
photo_regex = '<th>PHOTOURL</th> <td>(.*?)</td>'

#Extract the name and photo url using regex
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






#read in the dataset
with open("hawker-centres-geojson.geojson", "r") as inputfile:
	data = json.load(inputfile)



#extract required data for each line in dataset
hawker_centres = {}

for feature in data['features']:
	longitude = feature["geometry"]["coordinates"][0]
	latitude = feature["geometry"]["coordinates"][1]
	xml = feature["properties"]["Description"]

	name, photo_url = get_name_and_photo_url(xml)

	hawker_centres[name] = {"photo_url":photo_url, "latitude":latitude, "longitude":longitude}


#write out result
json_dataset = json.dumps(hawker_centres, indent = 4)
with open("json_dataset2.json", "w") as outfile:
	outfile.write(json_dataset)


