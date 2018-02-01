#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: channel.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-31 18:33:06
# Last Modified: 2018-01-31 18:34:04
#***********************************************

import threading

CH_NONE         = 0
CH_TCP_CLIENT   = 1
CH_UDP_CLIENT   = 2

CH_ERROR        = -1

def getBroadcastIPAddr(IPAddr):
        list = IPAddr.split('.')
        if len(list)== 4:
            list[3] = '255'
            host = '.'.join(list)
            return host
        return ''

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.port = 0
        self.host = ''
        self.client =None
        self.processResponse = None
        self.terminated = True
        self.channelType = CH_NONE
        self.daemon = True
    def openChannel(self,**kwargs):
        if 'port' in kwargs:
            self.port  = kwargs['port']
        if 'host' in kwargs:
            self.host = kwargs['host']

    def closeChannel(self):
        self.terminated = True




