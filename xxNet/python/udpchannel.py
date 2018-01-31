#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: udpchannel.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-31 18:32:31
# Last Modified: 2018-01-31 18:32:34
#***********************************************

from channel import *
import socket

class UDPClient(Client):

    def __init__(self):
        super(UDPClient,self).__init__()
        self.channelType = CH_UDP_CLIENT


    def openChannel(self,**kwargs):
        Client.openChannel(self,**kwargs)
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.terminated = False
            return True
        except socket.error:
            return False


    def write(self,data):
        if self.client and len(data) > 0:
            return  self.client.sendto(data, (self.host, self.port))
        return CH_ERROR


    def writeTo(self,toHost,port,data):
        if self.client and len(data) > 0:
            return  self.client.sendto(data, (toHost, port))
        return CH_ERROR


    def broadcast(self,data):
        host = getBroadcastIPAddr(self.host)
        return self.writeTo(host,self.port,data)


    def run(self):
        while not self.terminated:
            try:
                recvData = self.client.recv(1024)
                if recvData > 0 and self.processResponse:
                    self.processResponse(recvData)
            except socket.error:
                pass
        self.client.close()
