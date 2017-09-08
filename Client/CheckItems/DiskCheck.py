#!/usr/bin/python
#coding:utf8
#
#  磁盘检查
#
#
import psutil
from Interface import *


class DiskCheck(Interface):
    def check(self):
        data = {'item': 'disk'}
        disks = psutil.disk_partitions()
        disk_ios = psutil.disk_io_counters(perdisk=True)
        for item in disks:
            print item
            device, mountpoint,_,_ = item
            deviceName = str(device).split('/')[-1]
            total, used, free, percent = psutil.disk_usage(mountpoint)
            disk_io = disk_ios[deviceName]
            read_count = disk_io.read_count

            write_count = disk_io.write_count
            read_bytes = disk_io.read_bytes
            write_bytes= disk_io.write_bytes
            read_time= disk_io.read_time
            write_time= disk_io.write_time
            item_dic = {
                'total': total,
                'used': used,
                'free': free,
                'percent': percent,
                'read_count': read_count,
                'write_count': write_count,
                'read_bytes': read_bytes,
                'write_bytes': write_bytes,
                'read_time': read_time,
                'write_time': write_time
            }
            data[deviceName] = item_dic

        return data


if __name__ == '__main__':
    disk = DiskCheck()
    print disk.check()
