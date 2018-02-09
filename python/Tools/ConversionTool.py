#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: ConversionTool.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-09 11:26:49
# Last Modified: 2018-02-09 12:32:57
#***********************************************

#class 或对象 属相转化成dict 
def ObjToDir(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr

#dict 转化成object
def DirToObj(Dir):
    top = type('new', (object,), Dir)
    seqs = tuple, list, set, frozenset
    for i, j in Dir.items():
    	if isinstance(j, dict):
    	    setattr(top, i, DirToObj(j))
    	elif isinstance(j, seqs):
    	    setattr(top, i,
    		    type(j)(DirToObj(sj) if isinstance(sj, dict) else sj for sj in j))
    	else:
    	    setattr(top, i, j)
    return top
