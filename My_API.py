import simplejson
import urllib
import sys 
location_1 = open ('New Text Document (2).txt').readlines()
location_2 = open('New Text Document (3).txt').readlines()
out_file_name = 'C:\Users\User\Desktop\data_API.txt'
file = open(out_file_name, 'w')

locations_data = []
for row in location_1:
	loc_1 = row.strip()

	for column in location_2:
		loc_2 = column.strip()
		
		BASE  = "https://maps.googleapis.com/maps/api/elevation/json"
		url = BASE +"?locations=" + loc_1 + ',' + loc_2 + '&key=AIzaSyAQn03q5cWlfH15UiCWcUYToWDgW9hxJLs'
		locations_data.append(simplejson.load(urllib.urlopen(url)))
		
simplejson.dump(locations_data, file, indent=2)
