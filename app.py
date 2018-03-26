import psutil
import time


while True:
    # Get CPU percent
    data = psutil.cpu_percent()

    # Get disk usage
    # data = psutil.disk_partitions()

    # Get users who are logging in the terminal
    # data = psutil.users()

    print(data)
    time.sleep(30)
