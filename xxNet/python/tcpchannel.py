#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: tcpchannel.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-31 18:32:00
# Last Modified: 2018-01-31 18:32:12
#***********************************************



from channel import *
import datetime
import socket




class TCPClient(Client):

    def __init__(self):
        Client.__init__(self)
        self.channelType = CH_TCP_CLIENT



    def openChannel(self,**kwargs):
        Client.openChannel(self,**kwargs)
        try:
            address = (self.host,self.port)
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(address)
            self.terminated = False
            return True
        except socket.error:
            return False


    def write(self,data):
        if self.client and len(data) > 0:
            return  self.client.send(data)
        return CH_ERROR



    def run(self):
        while not self.terminated:
            try:
                recvData = self.client.recv(1024)
                if recvData > 0 and self.processResponse:
                    self.processResponse(recvData)
            except socket.error:
                pass
        self.client.close()

class NetClient(TCPClient):
    def __init__(self,processReceive):
        TCPClient.__init__(self)
        self.processResponse = processReceive

    def sendDataTo(self,**kwargs):
        if not self.openChannel(**kwargs):
            if self.processResponse:
                self.processResponse(False,'',message='Can not connect to printer!')
        else:
            if 'data' in kwargs:
                data = kwargs['data']
                count = self.client.send(data)
                if count == len(data):
                    startTime = datetime.datetime.now()
                    timeCount = 0
                    while timeCount < 3:
                        receive = self.client.recv(256)
                        if len(receive) > 0:
                            self.processResponse(True,receive,**kwargs)
                            self.closeChannel()
                            return
                        timeCount = (datetime.datetime.now() - startTime).seconds
            self.processResponse(False,'',message='Receive timeout!')
            self.closeChannel()
