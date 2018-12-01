"""
Use of sensor_switch and prox_interface to print proximity sensor measurements from the front and back sensors.
"""
from time import sleep
from prox_reader import ProxReader

FRONT = 1
BACK = 2

def main():
    reader = ProxReader('mm')

    while True:
        [front, back] = reader.measure()
        print("Front: {} mm".format(front))
        
        print("Back: {} mm".format(back))
        
        sleep(0.5)
        
if __name__ == "__main__":
    main()
