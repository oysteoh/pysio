#!/usr/bin/env python

import sys
import csv
from lib import barometer
from lib import temperature_humidity

if __name__ == '__main__':
    t = temperature_humidity.th02()
    h = barometer.hp206c()

    row = [t.getTemperature(), t.getHumidity()]
    with open('/home/pi/log.csv','a') as logfile:
        writer = csv.writer(logfile)
        writer.writerow(row)

    
    #print("Temp: %.2fC\tHumidity:%.2f" %
    #    (t.getTemperature(), t.getHumidity()), "%")
    #temp = h.ReadTemperature()
    #pressure = h.ReadPressure()
    #altitude = h.ReadAltitude()
    #print("Temperature\t: %.2f C\nPressure\t: %.2f hPa\nAltitude\t: %.2f m" %
    #    (temp, pressure, altitude))
