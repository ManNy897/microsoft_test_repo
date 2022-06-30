from queue import PriorityQueue
from geopy import distance
import json

def get_closest_hawker_locations(latitude, longitude):

	with open('json_dataset.json', 'r') as hawker_dataset:
	 	hawker_data = json.load(hawker_dataset)

	curr_location = (latitude, longitude)
	queue = PriorityQueue()
	for location_name in hawker_data:
		hawker_location = (hawker_data[location_name]["latitude"], hawker_data[location_name]["longitude"])
		hawker_photo = hawker_data[location_name]["photo_url"]
		
		#we store negative location so that value at front of queue will be largest and we can remove it
		dist = distance.distance(curr_location, hawker_location).miles * -1

		if(len(queue.queue) < 5):
			queue.put((dist, location_name, hawker_photo))
			continue;
		if queue.queue[0][0] < dist:
			queue.get()
			queue.put((dist,location_name, hawker_photo)) 

	print(queue.queue)

	return list(queue.queue)


