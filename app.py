import psutil
import time
import datetime


while True:
    # Get CPU percent
    # stat = psutil.cpu_percent()

    # Get disk usage
    stat = psutil.disk_partitions()

    # Get users who are logging in the terminal
    # stat = psutil.users()

    timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
    data = {"timestamp": timestamp, "stat": stat}
    print(data)

    time.sleep(30)
