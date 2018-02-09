#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: xxClient.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-07 14:29:04
# Last Modified: 2018-02-07 14:29:05
#***********************************************
"""
    sudo pip3 install requests
"""
# 导入 socket、sys 模块
import socket
import sys

import requests

class XXClient(object):
    """docstring for XXClient."""
    def __init__(self, arg):
        super(XXClient, self).__init__()
        self.arg = arg

    def localSocket(self,port):
        # 创建 socket 对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 获取本地主机名
        host = socket.gethostname()
        # 设置端口好
        # port = 9999
        # 连接服务，指定主机和端口
        s.connect((host, port))
        # 接收小于 1024 字节的数据
        msg = s.recv(1024)
        s.close()
        print (msg.decode('utf-8'))

    def get(self,url):
        # r = requests.get("http://45.77.151.91:8080/Virus/version.txt")
        r = requests.get(url)
        print(r.text)
        return r

    def post(self,url,postdata):
        # postdata = { 'uname':'fucker','upwd':'fucker' }
        # r = requests.post("http://45.77.151.91:9090/login",data=postdata)
        r = requests.post(url,data=postdata)
        print(r.text)
        return r

    def test(arg):
        client = XXClient("Test")
        # client.localSocket(9999)
        client.get("http://45.77.151.91:8080/Virus/version.txt")
        postdata = { 'uname':'fucker','upwd':'fucker' }
        client.post("http://45.77.151.91:9090/login",postdata)
