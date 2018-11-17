from smbus2 import SMBusWrapper

from time import sleep


with SMBusWrapper(1) as bus:
    while 1:
        data = bus.read_byte_data(0x70,0)
        print(data)
