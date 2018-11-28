"""
A class that abstracts the proximity sensor hardware interface and allows for the simultaneous return of front and back sensor measurements for the PowerPlant project
"""

from sensor_switch import MuxSwitcher
from prox_interface import ProxInterface

FRONT = 1
BACK = 2


class ProxReader(object):
    """
    Implementation of ProxReader functionality which includes taking a measurement from both the front and back sensors at the same time, and the ability to select which units should be returned.
    """

    def __init__(self, units):
        """
        Initializes the measurement with the desired units to return.
        Units options:
            'm'
            'cm'
            'mm' (default)
        """

        self.units = units

    def measure(self):
        """
        Takes measurement from front sensor and then switches to the back sensor. Though the measurements are not taken at the exact same time, the measurements should be close enough in time to serve the purpose of providing a distance measurement for the Power Plant project.
        """

        bus = MuxSwitcher()
        bus.sensor_select(FRONT)
        prox = ProxInterface()
        front = prox.read_prox()

        bus = MuxSwitcher()
        bus.sensor_select(BACK)
        prox = ProxInterface()
        back = prox.read_prox()
        if self.units == 'mm':
            front = front/1
            back = back/1
        elif self.units == 'cm':
            front = front/10
            back = back/10
        elif self.units == 'mm':
            front = front/100
            back = back/100
        else: # default unit is 'mm'
            front = front/1
            back = back/1

        return [front, back]
