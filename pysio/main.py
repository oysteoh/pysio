#!/usr/bin/env python

import sys
from lib import barometer
from lib import temperature_humidity

if __name__ == '__main__':
    t = temperature_humidity.th02()
    h = barometer.hp206c()

    with open('/home/pi/log.csv','a') as logfile:
         logfile.write(t.getTemperature() + "," + t.getHumidity())
    
    
    #print("Temp: %.2fC\tHumidity:%.2f" %
    #    (t.getTemperature(), t.getHumidity()), "%")
    #temp = h.ReadTemperature()
    #pressure = h.ReadPressure()
    #altitude = h.ReadAltitude()
    #print("Temperature\t: %.2f C\nPressure\t: %.2f hPa\nAltitude\t: %.2f m" %
    #    (temp, pressure, altitude))
