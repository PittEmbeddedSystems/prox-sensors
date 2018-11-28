"""
Use of sensor_switch and prox_interface to print proximity sensor measurements from the front and back sensors.
"""
from time import sleep
from sensor_switch import MuxSwitcher
from prox_interface import ProxInterface

FRONT = 1
BACK = 2

def main():
    bus = MuxSwitcher()
    while True:
        bus.sensor_select(FRONT)
        prox = ProxInterface()
        distance = prox.read_prox()
        print("Front: {} mm".format(distance))
        
        bus.sensor_select(BACK)
        prox = ProxInterface()
        distance = prox.read_prox()
        print("Back: {} mm".format(distance))
        
        sleep(0.5)
        
if __name__ == "__main__":
    main()
