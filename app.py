import datetime
import random
import os
import pprint
# import serial
import time


# ser = serial.Serial('/dev/ttyS1', 9600)
pp = pprint.PrettyPrinter(indent=2)


def get_temp():
    return random.randint(0, 50)

def get_humid():
    return random.randint(0, 50)

def get_current():
    return random.randint(-100, 100)


if __name__ == '__main__':

    while True:
        timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
        data = {
            "time": timestamp, 
            "temp": get_temp(),
            # "humid": get_humid(),
            # "current": get_current()
        }

        # pp.pprint(data)
        time.sleep(60)
