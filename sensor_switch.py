"""
Handles the selection of a sensor from those connected to the I2C bus via a mux
"""

from smbus2 import SMBus 

MUX_ADDRESS = 0x70
I2C_BUS = 1

class MuxSwitcher(object):
    """
    Implements an interface to the TCA9548A I2C switch. Use before taking a reading from an I2C device connected to the I2C switch.
    """
    def __init__(self):
        """
        Initialize the I2C bus via the TCA9548A hardware interface.
        """
        self.bus = SMBus(I2C_BUS)
        
    def sensor_select(self, sensorID):
        """
        Writes to the register n the I2C switch to select the desired sensor. Provide 1 for FRONT and 2 for BACK.
        """
        self.bus.write_byte_data(MUX_ADDRESS, 1, sensorID)
        return self.bus.read_byte_data(MUX_ADDRESS, 0)
