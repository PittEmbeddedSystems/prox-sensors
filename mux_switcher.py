from smbus2 import SMBusWrapper


with SMBusWrapper(1) as bus:

    bus.write_byte_data(0x70,1,1)
    bus.write_byte_data(0x70,1,0)

    bus.write_byte_data(0x70,2,0)
    bus.write_byte_data(0x70,35,1)
    #bus.write_byte_data(0x70,2,0)
