#!/usr/bin/python
#encoding:utf8
#  采集内存信息:已用内存、可用内存、空闲内存，单位是字节
#
#
from Interface import *
import psutil


class MemoryCheck(Interface):
    def check(self):
        m = psutil.virtual_memory()
        return {
            'item': 'memory',
            'free': m.free,
            'used': m.used,
            'available': m.available
        }
