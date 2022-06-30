from queue import PriorityQueue
from geopy import distance
import json

halfLat = 1.3609662013589499
halfLon = 103.842825001785

def getDatasetLocation(latitude, longitude):
	if(latitude <= halfLat and longitude >= halfLon):
		return "json_dataset1.json"
	if(latitude > halfLat and longitude >= halfLon):
		return "json_dataset2.json"
	if(latitude > halfLat and longitude < halfLon):
		return "json_dataset3.json"
	return "json_dataset4.json"

def get_closest_hawker_locations(latitude, longitude):

	#get the appropriate sub dataset based on longitude and latitude
	dataset_location = getDatasetLocation(float(latitude), float(longitude))

	with open(dataset_location, 'r') as hawker_dataset:
	 	hawker_data = json.load(hawker_dataset)

	curr_location = (latitude, longitude)
	queue = PriorityQueue()
	for location_name in hawker_data:
		hawker_location = (hawker_data[location_name]["latitude"], hawker_data[location_name]["longitude"])
		
		#we store negative location so that value at front of queue will be largest and we can remove it
		dist = distance.distance(curr_location, hawker_location).miles * -1
		hawker_photo = hawker_data[location_name]["photo_url"]

		if(len(queue.queue) < 5):
			queue.put((dist, location_name, hawker_photo))
			continue;
		if queue.queue[0][0] < dist:
			queue.get()
			queue.put((dist,location_name, hawker_photo)) 

	print(queue.queue)

	return list(queue.queue)


