import json
data = open ("C:\Users\User\Desktop\data_API.txt")
line_dict = json.load(data)
x=[]
y=[]
for ele in line_dict:

	for result in ele['results']:
		
		print result['elevation']