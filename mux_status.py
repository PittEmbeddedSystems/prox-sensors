from smbus2 import SMBusWrapper


with SMBusWrapper(1) as bus:

    print("start")
    print(bus.read_byte_data(0x70,0))
    print(bus.read_byte_data(0x70,1))
    print(bus.read_byte_data(0x70,2))
    print(bus.read_byte_data(0x70,3))
    print(bus.read_byte_data(0x70,4))
    print(bus.read_byte_data(0x70,5))
    print(bus.read_byte_data(0x70,6))
    print(bus.read_byte_data(0x70,7))


    bus.write_byte_data(0x70,1,1)
    bus.write_byte_data(0x70,2,1)
    bus.write_byte_data(0x70,3,1)
    bus.write_byte_data(0x70,4,1)
    bus.write_byte_data(0x70,5,1)
    bus.write_byte_data(0x70,6,1)
    bus.write_byte_data(0x70,7,1)
    bus.write_byte_data(0x70,8,6)

    print("after writing 1 to all registers:")
    
    print(bus.read_byte_data(0x70,0))
    print(bus.read_byte_data(0x70,1))
    print(bus.read_byte_data(0x70,2))
    print(bus.read_byte_data(0x70,3))
    print(bus.read_byte_data(0x70,4))
    print(bus.read_byte_data(0x70,5))
    print(bus.read_byte_data(0x70,6))
    print(bus.read_byte_data(0x70,7))
