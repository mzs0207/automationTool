#!/usr/bin/python
# coding:utf8
#
#  检查网络
#
from Interface import *
import psutil
import time


class NetworkCheck(Interface):

    def get_network_statistics(self):
        data = {}
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

    def check(self):
        data = {'item': 'network'}
        first = self.get_network_statistics()
        time.sleep(10)
        second = self.get_network_statistics()
        for item in first:
            sent = (second[item]['bytes_sent'] - first[item]['bytes_sent'])/10.0
            recv = (second[item]['bytes_recv'] - first[item]['bytes_recv'])/10.0
            data[item] = {
                'sent': sent,
                'recv': recv
            }

        return data


if __name__ == '__main__':
    nt = NetworkCheck()
    print nt.check()