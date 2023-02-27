import json
import requests


payload = 'lat-long-france-sample.csv'

url = "https://api.tollguru.com/v1/gps-tracks-csv-upload?vehicleType=2AxlesTruck"

headers = {
    'x-api-key': 'TOLLGURU_API_KEY',
    'Content-Type': 'text/plain'  # application/json
}

with open(payload, 'rb') as f:
    response = requests.request("POST", url, headers=headers, data=f)
    response = json.loads(response.text)
    print(response)
