#
#   所有实现检查项的类需要实现这个接口中的check方法
#   返回值包括两项:key 和 value
#
#


class interface(object):

    def check(self):
        '''
        如返回负载这个监控项
        return load,2
        '''
        pass