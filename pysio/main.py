#!/usr/bin/env python

import sys
import csv
import datetime
import smbus
from influxdb import InfluxDBClient
from lib import barometer
from lib import temperature_humidity

if __name__ == '__main__':
        # Get I2C bus
    bus = smbus.SMBus(1)

    # TH02 address, 0x40(64)
    # Select configuration register, 0x03(03)
    #		0x11(11)	Normal mode enabled, Temperature
    bus.write_byte_data(0x40, 0x03, 0x11)

    time.sleep(0.5)

    # TH02 address, 0x40(64)
    # Read data back from 0x00(00), 3 bytes
    # Status register, cTemp MSB, cTemp LSB
    data = bus.read_i2c_block_data(0x40, 0x00, 3)

    # Convert the data to 14-bits
    cTemp = ((data[1] * 256 + (data[2] & 0xFC))/ 4.0) / 32.0 - 50.0
    fTemp = cTemp * 1.8 + 32

    # TH02 address, 0x40(64)
    # Select configuration register, 0x03(03)
    #		0x01(01)	Normal mode enabled, Relative humidity
    bus.write_byte_data(0x40, 0x03, 0x01)

    time.sleep(0.5)

    # TH02 address, 0x40(64)
    # Read data back from 0x00(00), 3 bytes
    # Status register, humidity MSB, humidity LSB
    data = bus.read_i2c_block_data(0x40, 0x00, 3)

    # Convert the data to 12-bits
    humidity = ((data[1] * 256 + (data[2] & 0xF0)) / 16.0) / 16.0 - 24.0
    humidity = humidity - (((humidity * humidity) * (-0.00393)) + (humidity * 0.4008) - 4.7844)
    humidity = humidity + (cTemp - 30) * (humidity * 0.00237 + 0.1973)

    # Output data to screen
    print("Relative Humidity : %.2f %%" %humidity)
    print("Temperature in Celsius : %.2f C" %cTemp)
    print("Temperature in Fahrenheit : %.2f F" %fTemp)
    
    # t = temperature_humidity.th02()
    # h = barometer.hp206c()

    # print("Temp: %.2fC\tHumidity:%.2f" %(t.getTemperature(),t.getHumidity()),"%") 
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
