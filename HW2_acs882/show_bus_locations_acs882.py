from __future__ import print_function
import json
import os
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalid number of arguments.")
    sys.exit()

key = str(sys.argv[1])
LineRef = str(sys.argv[2])


url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s'%(key, LineRef)
response = urllib.urlopen(url)
data = response.read().decode('utf-8')
dataDict = json.loads(data)

numBuses = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print('Bus Line : ' + str(LineRef))
print('Number of Active Buses : ' + str(numBuses))

for i in range(numBuses):
    print('Bus', str(i), 'is at latitude',
    str((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])),
    'and longitude',
    str(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
