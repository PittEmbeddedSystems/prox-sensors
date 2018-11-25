from smbus2 import SMBusWrapper
from time import sleep
import VL53L1X



with SMBusWrapper(1) as bus:

    # enable register on mux to select a sensor
    bus.write_byte_data(0x70,1,2)

##    bus.write_byte_data(0x70,1,2)

    if bus.read_byte_data(0x70,2) == 0:
        exit(1)

    # configure the selected sensor
    tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
    tof.open() # initialize i2c bus and configure sensor
    tof.start_ranging(1) # start ranging, 1 = short range, 2 = medium, 3 = long
    sleep(0.3)
    distance_in_mm=tof.get_distance() # get range in mm
    print(distance_in_mm)
    # read from sensor   
    while 1:
        #distance_in_mm=tof.get_distance() # get range in mm
        #print(distance_in_mm)
##        data = bus.read_byte(0x29,0)
##        print(data)
##        data = bus.read_byte(0x29,1)
##        print(data)
        sleep(0.5)