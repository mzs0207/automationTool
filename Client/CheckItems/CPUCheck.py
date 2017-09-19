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
        cpu_count = psutil.cpu_count()
        if hasattr(cpuInfo, 'iowait'):
            return {
            "item": "cpu",
            "iowait": cpuInfo.iowait,
            "user": cpuInfo.user,
            "system": cpuInfo.system,
            "idle": cpuInfo.idle,
            "oneLoad":oneLoad,
            "fiveLoad":fiveLoad,
            "fifteenLoad":fifteenLoad,
            "count":cpu_count
            }
        else:
            return {
                "item": "cpu",
                "iowait": 0,
                "user": cpuInfo.user,
                "system": cpuInfo.system,
                "idle": cpuInfo.idle,
                "oneLoad": oneLoad,
                "fiveLoad": fiveLoad,
                "fifteenLoad": fifteenLoad,
                "count": cpu_count
            }