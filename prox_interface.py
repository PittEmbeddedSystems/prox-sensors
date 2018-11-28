"""
Implementation of interface to VL53L1X proximity sensor.
"""

import VL53L1X

SENSOR_ADDRESS = 0x29
I2C_BUS = 1
prox_range = 1

class ProxInterface(object):
    """
    Implementation of interface to sensor. For use with TCA9548A I2C switch, use sensor_switch first to select a sensor from the bus.
    """
    def __init__(self):
        """
        Initialize hardware interface.
        """
        self.prox = VL53L1X.VL53L1X(i2c_bus=I2C_BUS, i2c_address=SENSOR_ADDRESS)
        
    def read_prox(self):
        """
        Reads specified sensor with a predefined range.
        1 = short range (used for PowerPlant application)
        2 = medium range
        3 = long range
        
        Returns distance between sensor and object in mm.
        """
        self.prox.open()
        self.prox.start_ranging(prox_range)
        data = self.prox.get_distance()
        self.prox.close()
        return data
        
    
