#!/usr/bin/python
#coding:utf8
#
# 采集cpu信息
#
#
#
from Interface import *
import psutil
import os


class CPUCheck(Interface):

    def check(self):
        cpuInfo = psutil.cpu_times()
        oneLoad,fiveLoad, fifteenLoad = os.getloadavg()
        return {
            'item': 'cpu',
            'iowait': cpuInfo.iowait,
            'user': cpuInfo.user,
            'system': cpuInfo.system,
            'idle': cpuInfo.idle,
            'oneLoad':oneLoad,
            'fiveLoad':fiveLoad,
            'fifteenLoad':fifteenLoad
        }