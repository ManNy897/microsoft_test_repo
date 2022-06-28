from queue import PriorityQueue
from geopy import distance
import json

def get_closest_hawker_locations(latitude, longitude):

	with open('json_dataset.json', 'r') as fcc_file:
	 	hawker_data = json.load(fcc_file)

	curr_location = (latitude, longitude)
	queue = PriorityQueue()
	for location_name in hawker_data:
		hawker_location = (hawker_data[location_name]["latitude"], hawker_data[location_name]["longitude"])
		dist = distance.distance(curr_location, hawker_location).miles * -1
		hawker_photo = hawker_data[location_name]["photo_url"]

		if(len(queue.queue) <= 5):
			queue.put((dist, location_name, hawker_photo))
			continue;
		if queue.queue[0][0] < dist:
			queue.get()
			queue.put((dist,location_name, hawker_photo)) 
			
	print(queue.queue)

	return list(queue.queue)


