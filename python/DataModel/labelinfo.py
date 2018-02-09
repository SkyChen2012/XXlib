#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: labelinfo.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-06 13:23:51
# Last Modified: 2018-02-06 13:23:53
#***********************************************



class labelInfo(object):

    # SN码
    SN = ""
    # 验证码
    YZM = ""
    # 时间 --（data time）
    DT = ""
    # 产品型号 --（Product typt）
    PT = ""
    # 存档
    save = ""

    """docstring for labelInfo."""
    def __init__(self):
        super(labelInfo, self).__init__()

    def toString(self):
        return ('[SN -> ',self.SN,'][YZM -> ',self.YZM,'][DT -> ',self.DT,'][PT -> ',self.PT,'][save -> ',self.save,']')

    def toJsonStr(self):
        print("toJsonStr ... ")

    def toDir(self):
        print("toDir ... ")

    def saveToSql(self):
        print("save To Sql ... ")

    def defaut(self):
        self.save = "save"
        self.PT = "PT"
        self.DT = "DT"
        self.YZM = "YZM"
        self.SN = "SN"
        return self


