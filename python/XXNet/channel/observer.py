#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: observer.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-31 18:32:44
# Last Modified: 2018-01-31 18:32:47
#***********************************************

class Subject(object):
    observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self,observer):
        if self.observers.index(observer) >=  0:
            self.observers.remove(observer)

    def notify(self,event,*args,**kwargs):
        for observer in self.observers:
            observer.selfUpdate(event,*args,**kwargs)



class Observer(object):
    def selfUpdate(self,event,*args,**kwargs):
        pass
