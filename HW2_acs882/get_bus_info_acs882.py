from __future__ import print_function
import json
import os
import sys
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments.")
    sys.exit()

key = str(sys.argv[1])
LineRef = str(sys.argv[2])
newFile = str(sys.argv[3])

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(key, LineRef)
response = urllib.urlopen(url)
data = response.read().decode('utf-8')
dataDict = json.loads(data)
numBuses = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

busInfo = open(newFile, 'w')

busInfo.write('Latitude,Longitude,Stop Name,Stop Status\n')

for i in range(numBuses):
    latitude =  str((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    longitude = str((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    destName = (dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
    destDist =(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    busInfo.write(latitude + ',' + longitude + ',' + destName + ',' + destDist + '\n')
