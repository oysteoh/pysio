#!/usr/bin/env python

import sys
import csv
import datetime
from influxdb import InfluxDBClient
from lib import barometer
from lib import temperature_humidity

if __name__ == '__main__':
    t = temperature_humidity.th02()
    h = barometer.hp206c()

    print("Temp: %.2fC\tHumidity:%.2f" %(t.getTemperature(),t.getHumidity()),"%") 
    # time = datetime.datetime.utcnow()
    # dbclient = InfluxDBClient('10.0.0.2', 8086, 'root', 'root', 'pysio')
# 
    # json_body = [{
    #     "measurement": "humidity",
    #     "tags": {
    #         "place": "home",
    #         "room": "shed"
    #     },
    #     "fields": {
    #         "value": t.getHumidity()
    #     }
    # }, {
    #     "measurement": "temperature",
    #     "tags": {
    #         "place": "home",
    #         "room": "shed"
    #     },
    #     "fields": {
    #         "value_1": t.getTemperature(),
    #         "value_2": h.ReadTemperature()
    #     }
    # }, {
    #     "measurement": "pressure",
    #     "tags": {
    #         "place": "home",
    #         "room": "shed"
    #     },
    #     "fields": {
    #         "value": h.ReadPressure()
    #     }
    # }]

    # dbclient.write_points(json_body)

    # row = [datetime.datetime.utcnow(), t.getTemperature(), h.ReadTemperature(), t.getHumidity(), h.ReadPressure()]
    # with open('/home/pi/log.csv','a') as logfile:
    #    writer = csv.writer(logfile)
    #    writer.writerow(row)
