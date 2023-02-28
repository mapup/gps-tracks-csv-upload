# gps-tracks-csv-upload & gps-tracks-csv-dwonload
Use TollGuru "GPS tracks Toll API" endpoint to calculate tolls after you make the trip. 

You can upload your GPS tracks (in CSV format) to receive tolls for the route matched using the GPS tracks. You can
* Based on vehicles in use in each country, [vehicle type support](https://github.com/mapup/tollguru_vehicle_coverage/wiki/Vehicle-types-supported-by-TollGuru). For example, you can receive tolls for vehicles based on axle counts for cars, SUV, pick-up, trucks (up to 9-axles), motorcycle, bus, motorhome, RV, limousine.
* Specify parameters such as weight and height to receive tolls based on the specified parameters
* Specify the timestamp of each GPS trace. If you do not specify the timestamp, tolls are likely to be inaccurate on time-based-toll facilities.
* Specify whether you want to receive toll information immediately (isAsync=false) or can wait (isAsync=true). Use the asynchronous mode when uploading multiple or large GPS track files. Response in asynchronous mode comes with a requestId and a requestedTimestamp. If you are setting isAsync=true, pass the result you are getting from the function `gps_tracks_csv_upload` to the function `gps_tracks_csv_dwonload` to get the result. These results would be available for download for up to 30 days.
