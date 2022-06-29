import json
import csv
import re

# import xml.etree.ElementTree as ET
# from lxml import etree


name_regex = '<th>NAME</th> <td>(.*?)</td>'
photo_regex = '<th>PHOTOURL</th> <td>(.*?)</td>'

with open("hawker-centres-geojson.geojson", "r") as inputfile:
	data = json.load(inputfile)

hawker_centres = {}
hawker_centers_list = []

for feature in data['features']:
	# try:
		longitude = feature["geometry"]["coordinates"][0]
		latitude = feature["geometry"]["coordinates"][1]
		xml = feature["properties"]["Description"]

		name_regex_result = re.search(name_regex, xml, re.IGNORECASE)
		name = None
		if name_regex_result != None:
			name = name_regex_result.group(1)
		else:
			print("no name")


		photo_regex_result = re.search(photo_regex, xml, re.IGNORECASE)
		photo_url = None
		if photo_regex_result != None:
			photo_url = photo_regex_result.group(1)
		else:
			print("no photo")

		# print(xml)
		# root = etree.fromstring(xml)
		# name = root.xpath('.//table/tr/th[text()="NAME"]/../td')[0].text
		# photo_url = root.xpath('.//table/tr/th[text()="PHOTOURL"]/../td')[0].text
		hawker_centres[name] = {"photo_url":photo_url, "latitude":latitude, "longitude":longitude}
		hawker_centers_list.append([name, photo_url, longitude, latitude])
print(len(hawker_centres))

json_dataset = json.dumps(hawker_centres, indent = 4)
with open("json_dataset.json", "w") as outfile:
	outfile.write(json_dataset)


