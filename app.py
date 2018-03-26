import psutil
import time
import datetime


while True:
    # Get CPU percent
    data = psutil.cpu_percent()

    # Get disk usage
    # data = psutil.disk_partitions()

    # Get users who are logging in the terminal
    # data = psutil.users()

    timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print("Data: %s, Timestamp: %s" % (data, timestamp))
    time.sleep(30)
