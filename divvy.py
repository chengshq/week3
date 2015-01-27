# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import json
import math
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

distance = float(99999999999999)
for station in stations:
	Young_lat = 41.793414
	Young_long = -87.600915
	new_distance = math.sqrt((station['latitude']-Young_lat)**2 + (station['longitude']-Young_long)**2)

	if new_distance < distance:
		distance = new_distance
		closest_station = station['stationName']
		station_available_bikes = station['availableBikes']

print("The closest Divvybikes station to Young Building is:", closest_station + ".")
print("There are", station_available_bikes, "bikes currently available.")




# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes like x and y coordinates, and calculate distance between locations with the usual Euclidean distance formula.

# 1. Modify the code above to display the station name and number of available bikes for the station closest to Young.

# You will likely want to consult the JSON stream from Divvy

# - http://www.divvybikes.com/stations/json
