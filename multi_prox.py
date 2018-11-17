from smbus2 import SMBusWrapper

from time import sleep

##read from first sensor, wait, then read from second
with SMBusWrapper(1) as bus:
    bus.write_byte_data(0x70,0,1)
    bus.write_byte_data(0x70,1,1)
    while 1:
        data = bus.read_byte(0x29,0)
        print(data)
        data = bus.read_byte(0x29,1)
        print(data)
        sleep(.5)
