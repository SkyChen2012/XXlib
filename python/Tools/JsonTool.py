#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: JsonTool.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-09 09:41:54
# Last Modified: 2018-02-09 09:41:57
#***********************************************
"""
JSON 解码为 Python 类型转换对应表：
    JSON	           Python
    object	           dict
    array	           list
    string	           str
    number (int)	   int
    number (real)	   float
    true	           True
    false       	   False
    null	           None
"""

import json
import codecs

# from DataModel.labelinfo import *
# from Tools import ConversionTool


# Python 字典类型转换为 JSON 对象
def PythonDirToJson(data):
    # Python 字典类型转换为 JSON 对象
    # data = {
    #     'no' : 1,
    #     'name' : 'Runoob',
    #     'url' : 'http://www.runoob.com'
    # }

    json_str = json.dumps(data)
    print ("Python 原始数据：", repr(data))
    print ("JSON 对象：", json_str)
    return json_str

def JsonToPythonDir(json_str):
    # 将 JSON 对象转换为 Python 字典
    # json_str = '{"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}'
    dataDir = json.loads(json_str)
    # print ("data2['name']: ", data2['name'])
    # print ("data2['url']: ", data2['url'])
    print("dataDir ==> ",dataDir)
    return dataDir


def lableinfoTest(lableinfo):
    fd = codecs.open('/Users/Benson/Desktop/demo.js')
    text = fd.read()
    print(text)
    # label = labelInfo()
    # label.defaut()
    # print("Class ==> ", dir(ConversionTool.DirToObj(JsonToPythonDir(PythonDirToJson(ConversionTool.ObjToDir(label))))))

self.lableinfoTest()