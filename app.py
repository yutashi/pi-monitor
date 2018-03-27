import pprint
import psutil
import time
import datetime


pp = pprint.PrettyPrinter(indent=2)


while True:
    # Get CPU percent
    # stat = psutil.cpu_percent()

    # Get disk usage
    stat = psutil.disk_usage('/')

    # Get users who are logging in the terminal
    # stat = psutil.users()

    timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
    data = {"timestamp": timestamp, "stat": stat}
    pp.pprint(data)

    time.sleep(30)
