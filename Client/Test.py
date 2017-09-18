#!/usr/bin/python
# coding:utf8
from apscheduler.schedulers.background import BackgroundScheduler
from CheckItems.CPUCheck import CPUCheck
from CheckItems.DiskCheck import DiskCheck
from CheckItems.MemoryCheck import MemoryCheck
from CheckItems.NetworkCheck import NetworkCheck
from CheckItems.NetworkConnectionsCheck import NetworkConnections
from Post import post
import os
import time
from Scheduler import *
import datetime


def tick(checkItem):

    data = checkItem.check()
    post(data, '/checkData')


if __name__ == '__main__':

    '''
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, args=(CPUCheck(),), trigger='interval', seconds=30)
    scheduler.add_job(lambda:tick(MemoryCheck()), 'interval', seconds= 60)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        while True:
            time.sleep(2)
            print 'sleep'
    except Exception,e:
        print e
        scheduler.shutdown()
    '''
    scheduler = Scheduler()
    scheduler.start()
    while 1:
        print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(30)
