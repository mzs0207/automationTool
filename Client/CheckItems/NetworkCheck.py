#!/usr/bin/python
# coding:utf8
#
#  检查网络
#
from Interface import *
import psutil


class NetworkCheck(Interface):

    def check(self):
        data = {'item': 'network'}
        network_data = psutil.net_io_counters(pernic=True)

        for item in network_data:
            bytes_sent, bytes_recv, packets_sent, packets_recv, errin, errout, dropin, dropout =network_data[item]
            data[item] = {
                'bytes_sent': bytes_sent,
                'bytes_recv': bytes_recv,
                'packets_sent': packets_sent,
                'packets_recv': packets_recv,
                'errin': errin,
                'errout': errout,
                'dropin': dropin,
                'dropout':dropout
            }
        return data


if __name__ == '__main__':
    nt = NetworkCheck()
    print nt.check()