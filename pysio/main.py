#!/usr/bin/env python

import sys
import csv
import datetime
import time
import smbus2 as smbus

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
    
    # HP206C address, 0x76(118)
    # Send OSR and channel setting command, 0x44(68)
    bus.write_byte(0x76, 0x44 | 0x00)

    time.sleep(0.5)

    # HP206C address, 0x76(118)
    # Read data back from 0x10(16), 6 bytes
    # cTemp MSB, cTemp CSB, cTemp LSB, pressure MSB, pressure CSB, pressure LSB
    data = bus.read_i2c_block_data(0x76, 0x10, 6)

    # Convert the data to 20-bits
    cTemp2 = (((data[0] & 0x0F) * 65536) + (data[1] * 256) + data[2]) / 100.00
    pressure = (((data[3] & 0x0F) * 65536) + (data[4] * 256) + data[5]) / 100.00

    # HP206C address, 0x76(118)
    # Send OSR and channel setting command, 0x44(68)
    bus.write_byte(0x76, 0x44 | 0x01)

    time.sleep(0.5)

    # HP206C address, 0x76(118)
    # Read data back from 0x31(49), 3 bytes
    # altitude MSB, altitude CSB, altitude LSB
    data = bus.read_i2c_block_data(0x76, 0x31, 3)

    # Convert the data to 20-bits
    altitude = (((data[0] & 0x0F) * 65536) + (data[1] * 256) + data[2]) / 100.00

    # Output data to screen
    print("Altitude : %.2f m" %altitude)
    print("Pressure : %.2f Pa" %pressure)
    print("Temperature in Celsius : %.2f C" %cTemp2)

    with open("~/log_file.txt", "w") as log_file:
        log_file.write(int(cTemp2))

   
