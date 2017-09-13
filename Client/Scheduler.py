#!/usr/bin/python
# coding:utf8
#
#
#   任务调度：收集信息、普通任务调度
#
#
from Post import post
from apscheduler.schedulers.background import BackgroundScheduler
from CheckItems.CPUCheck import CPUCheck
from CheckItems.DiskCheck import DiskCheck
from CheckItems.MemoryCheck import MemoryCheck
from CheckItems.NetworkCheck import NetworkCheck
from CheckItems.NetworkConnectionsCheck import NetworkConnections


def tick(checkItem, url):

    data = checkItem.check()
    post(data, url)


class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.init_add_scheduler()

    def init_add_scheduler(self):
        self.scheduler.add_job(tick, args=(CPUCheck(), '/checkData'), trigger='interval', id='cpu', seconds=60, max_instances=1)
        self.scheduler.add_job(tick, args=(DiskCheck(), '/checkData'), trigger='interval', id='disk', seconds=600, max_instances=1)
        self.scheduler.add_job(tick, args=(MemoryCheck(),'/checkData'), trigger='interval', id='memory', seconds=60, max_instances=1)
        self.scheduler.add_job(tick, args=(NetworkConnections(),'/checkData'), trigger='interval', id='networkConnections', seconds=60, max_instances=1)
        self.scheduler.add_job(tick, args=(NetworkCheck(),'/checkData'), trigger='interval', id='network', seconds=60, max_instances=1)

    def start(self):
        self.scheduler.start()


