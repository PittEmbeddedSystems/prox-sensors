import VL53L1X

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # initialize i2c bus and configure sensor
tof.start_ranging(1) # start ranging, 1 = short range, 2 = medium, 3 = long
while True:
    distance_in_mm=tof.get_distance() # get range in mm
    print(distance_in_mm)
tof.stop_ranging() # stop ranging
