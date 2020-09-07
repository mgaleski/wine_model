import requests
import json

# Flask URL
url = 'http://0.0.0.0:5000/api'

#Sample datapoints for a wine to be passed to model
data = [[8.1, 0.38, 0.28, 2.1, .066, 13, 30, 0.9968, 3.23, 0.75, 9.7, 7]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

#Post request sent to flask app
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
