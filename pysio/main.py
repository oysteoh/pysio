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
    time = datetime.datetime.utcnow()
    dbclient = InfluxDBClient('10.0.0.2', 8086, 'root', 'root', 'pysio')

    json_body = [{
        "tags": {
            "placement": "shed",
            "type": "humidity"
        },
        "measurement": "luftfuktighet_bod",
        "time": time,
        "fields": {
            "Float_value": t.getHumidity()
        }
    },    {
         "tags": {
            "placement": "shed",
            "type": "temperature_0"
        },
        "measurement": "temperatur_0_bod",
        "time": time,
        "fields": {
            "Float_value": t.getTemperature()
        }
    }, {
         "tags": {
            "placement": "shed",
            "type": "temperature_1"
        },
        "measurement": "temperatur_1_bod",
        "time": time,
        "fields": {
            "Float_value": h.ReadTemperature()
        }
    }, {
         "tags": {
            "placement": "shed",
            "type": "pressure"
        },
        "measurement": "barometertrykk",
        "time": time,
        "fields": {
            "Float_value": h.ReadPressure()
        }
    }]

    dbclient.write_points(json_body)



    # row = [datetime.datetime.utcnow(), t.getTemperature(), h.ReadTemperature(), t.getHumidity(), h.ReadPressure()]
    # with open('/home/pi/log.csv','a') as logfile:
    #    writer = csv.writer(logfile)
    #    writer.writerow(row)
