#!/usr/bin/python
#coding:utf8
#
#  收集网络连接信息
#
#

from Interface import *
import psutil
import heapq


class NetworkConnections(Interface):
    def check(self):
        data = {'item' : 'networkConnection'}
        connections = psutil.net_connections()
        state = {}
        remote_hosts = {}

        for item in connections:
            c_state = item.status
            if len(item.raddr) == 0:
                continue
            r_ip = item.raddr.ip

            if c_state in state:
                state[c_state] += 1
            else:
                state[c_state] = 1

            if r_ip in remote_hosts :
                remote_hosts[r_ip] += 1
            else:
                remote_hosts[r_ip] = 1

        ip_10 = heapq.nlargest(10, remote_hosts, key= lambda k: remote_hosts[k])
        remote_hosts_10 = []
        for ip in ip_10:
            remote_hosts_10.append({'ip':ip, 'count':remote_hosts[ip]})
        data['hosts'] = remote_hosts_10
        data['status'] = state

        return data


if __name__ == '__main__':
    conn = NetworkConnections()
    print conn.check()
