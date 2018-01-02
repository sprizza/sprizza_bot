web: python mio_bot.py --log file -
mio_bot.py
import sys
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    try:
        request = requests.get(url='https://royal-tag-services.herokuapp.com/api/sms-service/scheduler/')
    except Exception as e:
        print >>sys.stderr, 'scheduler request failed'

sched.start()
