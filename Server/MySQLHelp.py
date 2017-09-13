#!/usr/bin/python
# coding:utf8
#
#  操作mysql
#
import MySQLdb
from config import config
import traceback


class MySQLHelp:
    def __init__(self):
        self.conn = None

    def get_conn(self):
        if self.conn is not None:
            try:
                self.conn.ping()
                return self.conn
            except Exception,e:
                traceback.print_exc()
        try:
            self.conn = MySQLdb.connect(host = config['mysql_ip'],
                                           port = config['mysql_port'],
                                           user = config['mysql_user'],
                                           passwd = config['mysql_passwd'],
                                           db = config['database'],
                                           charset = 'utf8'
                                           )
            return self.conn
        except Exception, e:
            print e

    def save_cpu(self, host,rtime, iowait, user, system, idle, oneLoad, fiveLoad, fifteenLoad):
        sql = "replace into cpu(host,rtime, iowait, user, system, idle, oneLoad, fiveLoad, fifteenLoad) value('%s','%s',%s, %s,%s,%s,%s,%s,%s)" %(host,rtime, iowait, user, system, idle, oneLoad, fiveLoad, fifteenLoad)
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def save_disk(self, host, rtime, total, used, free, percent,
                  read_count, write_count, read_bytes, write_bytes,
                  read_time, write_time):
        sql = "replace into disk(host, rtime, total, used, free, percent, read_count, write_count, read_bytes, write_bytes, read_time, write_time) values "
        sql += " ('%s', '%s', %s,%s,%s,%s,%s,%s,%s, %s,%s,%s)" %(host, rtime, total, used, free, percent,
                                                                read_count, write_count, read_bytes, write_bytes,
                                                                read_time, write_time)
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def save_memory(self, host, rtime, free, used, available):
        sql = "replace into Memory(host, rtime, free, used, available) values('%s', '%s', %s,%s,%s)" %(host, rtime, free, used, available)
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def save_Network(self, host, rtime, nic, sent, recv):
        sql = "replace into Network(host, rtime, nic, sent, recv) values ('%s', '%s', '%s', %s, %s)" %(host, rtime, nic, sent, recv)
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
