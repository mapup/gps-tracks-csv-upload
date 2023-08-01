import json
from time import sleep
import requests

# API key for Tollguru
TOLLGURU_API_KEY = "YOUR_TOLLGURU_API_KEY"

# Upload CSV file - You can use the CSV format file as shown in the table below.
def gps_tracks_csv_upload(isAsync="false"):
    payload = 'lat-long-france-sample.csv'

    url = f"https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload?isAsync={isAsync}&weight=30000&height=10&vehicleType=5AxlesTruck&vehicleName=123456"

    headers = {
        'x-api-key': TOLLGURU_API_KEY,
        'Content-Type': 'text/csv'
    }

    with open(payload, 'rb') as f:
        response = requests.request("POST", url, headers=headers, data=f)
        # response = json.loads(response.text)
    return response

# When isAsync is set to true, use this funcation to get the result by passing the return value from the gps_tracks_csv_upload
def gps_tracks_csv_download(response_from_gps_tracks_csv_upload, retry, delay: int):
    count = retry # number of retries before stoping
    status = "ERROR"
    while count >= 0 and status == "ERROR" :
        url = "https://apis.tollguru.com/toll/v2/gps-tracks-csv-download"

        headers = {
            'x-api-key': TOLLGURU_API_KEY,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=response_from_gps_tracks_csv_upload)
        response = json.loads(response.text)
        status = response['status']
        count -= 1
        sleep(delay) # delay between each request.
    return response

# print(gps_tracks_csv_upload())
# print(gps_tracks_csv_download(response_from_gps_tracks_csv_upload=gps_tracks_csv_upload(isAsync="true"), retry=5, delay=5))
