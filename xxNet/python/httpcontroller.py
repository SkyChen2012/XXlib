#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: httpcontroller.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-31 18:32:56
# Last Modified: 2018-01-31 18:34:57
#***********************************************

from const import *
import threading
import urllib2


import pycurl,os
from StringIO import StringIO

#from encode import multipart_encode
#from streaminghttp import register_openers


HTTP_URL_OPEN_TIMEOUT  = 5
HTTP_CONNECT_TIMEOUT  = 10
HTTP_RESPONSE_OK      = 200



class Controller (ObjectController):
    def __init__(self):
        self.id = 0
        self.thread=None
        self.URL = ''
        self.event   = EVENT_NONE
        self.updated = False
        self.errorCode = ERROR_CODE_UNKNOWN
        self.flag = 0
        self.cached = False
        self.params = {}
        self.fields = []
        self.notifyResult = None

    def update(self):
        pass

    def post(self):
        pass

    def notifyProgress(self,percent):
        pass

    def processResponse(self,result,response,**kwargs):
        if self.notifyResult:
            self.notifyResult(result,response,**kwargs)


class JSONController(Controller):
    def update(self):
        if len(self.URL)>0:
            self.thread = RequestThread(self)
            self.thread.start()


    def post(self):
        if len(self.URL)>0:
            self.thread = PostThread(self)
            self.thread.start()



    
class FileController(Controller):
    def update(self):
        if len(self.URL)>0:
            self.thread = DownloadThread(self)
            self.thread.start()

    def post(self):
        if len(self.URL)>0:
            self.thread = UploadThread(self)
            self.thread.start()




class TextController(FileController):
    def __init__(self):
        FileController.__init__(self)
        self.text = None

    def __fileExists(self):
        filePathName = getUserPath(self.URL)
        return os.path.isfile(filePathName)

    def loadFromFile(self):
        filePathName = getUserPath(self.URL)
        if os.path.isfile(filePathName):
            file = open(filePathName)
            try:
                self.text = file.read()
            finally:
                file.close()
            return True
        return False

    def update(self,**kwargs):
        toUpdate = False
        if 'update' in kwargs:
            toUpdate = kwargs.get('update',False)
        if toUpdate:
            FileController.update(self)
        else:
            if  self.loadFromFile():
                self.updated = True
                self.processResponse(True,'')
            else:
                FileController.update(self)

    def processResponse(self,result,response,**kwargs):
        self.loadFromFile()
        if self.notifyResult:
            self.notifyResult(result,response,**kwargs)



#threads for http get or post


class HttpThread(threading.Thread):
    def __init__(self,controller):
        threading.Thread.__init__(self)
        self.controller = controller

    def processResponse(self,result,response,**kwargs):
        self.controller.processResponse(result,response,**kwargs)


class RequestThread(HttpThread):
    def run(self):
        response = ''
        url = URL(self.controller.URL) +'?'+ urllib.urlencode(self.controller.params)
        try:
            request = urllib2.Request(url)
            resData = urllib2.urlopen(request,timeout = HTTP_URL_OPEN_TIMEOUT)
            response = resData.read()
            resData.close()
            result = True
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                result = False
            elif hasattr(e,"code"):
                result = False
            else:
                result = False
        self.processResponse(result,response)


class PostThread(HttpThread):
    def __init__(self,controller):
        HttpThread.__init__(self,controller)
    def run(self):
        result = False
        response = ''
        try:
            paraData = urllib.urlencode(self.controller.params)
            info = urllib2.urlopen(URL(self.controller.URL), paraData,timeout = HTTP_URL_OPEN_TIMEOUT)
            response = info.read()
            info.close()
            result = True
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                result = False
            elif hasattr(e,"code"):
                result = False
            else:
                result = False
        self.processResponse(result,response)



class DownloadThread(HttpThread):

    def __urlCallback(self,already,size,totalSize):
        prec = 0
        if totalSize > 0 :
            prec =100.0*already*size/totalSize
            if 100 < prec:
                prec = 100
        if  self.controller.notifyProgress:
            self.controller.notifyProgress(prec)

    def run(self):
        result = False
        response = ''
        savePath =getUserPath(self.controller.URL)
        url = FileURL(self.controller.URL)
        try:
            urllib.urlretrieve(url ,savePath ,self.__urlCallback)
            result = True
        except IOError:
            result = False

        self.processResponse(result,response)


class UploadThread(HttpThread):
    def __urlCallback(self,download_t,download_d,upload_totalSize,upload_already):
        prec = 0
        if upload_totalSize > 0 :
            prec =100.0 * upload_already/upload_totalSize
            if 100 < prec:
                prec = 100

        if  self.controller.notifyProgress:
            self.controller.notifyProgress(prec)



    def run(self):

        c = pycurl.Curl()
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.URL, URL(self.controller.URL))

        
        c.setopt(pycurl.NOPROGRESS, 0)
        c.setopt(pycurl.PROGRESSFUNCTION, self.__urlCallback)
        c.setopt(pycurl.CONNECTTIMEOUT,HTTP_CONNECT_TIMEOUT)
        c.setopt(pycurl.CONNECTTIMEOUT,HTTP_CONNECT_TIMEOUT)

        c.setopt(pycurl.HTTPPOST, self.controller.fields)

        response_buf = StringIO()
        c.setopt(pycurl.WRITEDATA, response_buf)

        response_code = 0
        try:
            c.perform()
            response_code = c.getinfo(pycurl.RESPONSE_CODE)
            result = (response_code == HTTP_RESPONSE_OK)
        except  pycurl.error:
            result = False
        response = response_buf.getvalue()
        self.processResponse(result,response,message = '(%d)' % response_code)
        
        c.close()



#class UploadThread(HttpThread):
#    def run(self):
#        response = ''
#        register_openers()
#        datagen, headers = multipart_encode(self.controller.params)
#        request = urllib2.Request(URL(self.controller.URL), datagen, headers)
#        try:
#            info = urllib2.urlopen(request)
#            response = info.read()
#            info.close()
#            result = True
#        except urllib2.URLError,e:
#            if hasattr(e,"reason"):
#                result = False
#            elif hasattr(e,"code"):
#                result = False
#            else:
#                result = False
#        self.processResponse(result,response)

