#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: udp_gb_server.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-01 09:47:03
# Last Modified: 2018-02-02 13:06:26
#***********************************************

# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 5354

network = '224.0.0.251'


def fun_timer():
    s.sendto('Client broadcast message! ^_^!!!!'.encode('utf-8'), (network, PORT))
    print('Hello Timer!')
    global timer
    timer = threading.Timer(0.5, fun_timer)
    timer.start()


timer = threading.Timer(1, fun_timer)
timer.start()




