#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: config.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-09 10:18:37
# Last Modified: 2018-02-09 10:18:39
#***********************************************
"""
    sudo pip3 install configparser
"""

import os
import configparser

#获取文件的当前路径（绝对路径）
cur_path=os.path.dirname(os.path.realpath(__file__))

#获取config.ini的路径
def GetConfig(arg):
     config_path=os.path.join(cur_path,'config.ini')
     conf=configparser.ConfigParser()
     conf.read(config_path)
     mail_server=conf.get('email', 'mail_server')
     mail_username=conf.get('email', 'mail_username')
     mail_password=conf.get('email', 'mail_password')
     mail_receiver=conf.get('email', 'mail_receiver')
     return mail_server

print(GetConfig(2))
