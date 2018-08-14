#!/usr/bin/env python

import sys
import csv
from lib import barometer
from lib import temperature_humidity

if __name__ == '__main__':
    t = temperature_humidity.th02()
    h = barometer.hp206c()

    row = [t.getTemperature(), h.ReadTemperature(), t.getHumidity(), h.ReadPressure()]
    with open('/home/pi/log.csv','a') as logfile:
        writer = csv.writer(logfile)
        writer.writerow(row)

