# request.py requests the server for the predictions

# import libraries
import requests
url = 'http://localhost:5000/api'
r = requests.post(url, json={'measurements':[1,1,1,1]})
print(r.json())