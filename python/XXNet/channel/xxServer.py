#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: xxServer.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-07 14:26:36
# Last Modified: 2018-02-07 14:26:38
#***********************************************

# 导入 socket、sys 模块
import socket
import sys

class XXServer(object):
    
    """docstring for XXServer."""
    def __init__(self, arg):
        super(XXServer, self).__init__()
        self.arg = arg

    def serverStart(arg):
        # 创建 socket 对象
        serversocket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
        # 获取本地主机名
        host = socket.gethostname()
        port = 9999
        # 绑定端口
        serversocket.bind((host, port))
        # 设置最大连接数，超过后排队
        serversocket.listen(5)
        while True:
            # 建立客户端连接
            clientsocket,addr = serversocket.accept()
            print("连接地址: %s" % str(addr))
            msg='欢迎访问菜鸟教程！'+ "\r\n"
            clientsocket.send(msg.encode('utf-8'))
            clientsocket.close()
