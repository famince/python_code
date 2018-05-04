#!/usr/bin/python
#coding:UTF-8
import urllib2
import json
from urllib import urlencode
from urllib import quote


class Youdao:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/openapi.do'
        self.key = '993123434'  #有道API key
        self.keyfrom = 'pdblog' #有道keyfrom

    def get_translation(self,words):
        url = self.url + '?keyfrom=' + self.keyfrom + '&key='+self.key + '&type=data&doctype=json&version=1.1&q=' + words
        result = urllib2.urlopen(url).read()
        json_result = json.loads(result)
        translations = json_result["translation"]
        for t in translations:
            print t

        if 'basic' in json_result:
            basics = json_result['basic']
            for (k,v) in basics.items():
                if 'explains' == k:
                  print k
                  for explain in v:
                      print explain
                else:
                    print k + ": " + v;


youdao = Youdao()
while True:
     msg = raw_input()

     # 先把string转化为unicode对象，再编码为utf-8.若没有此行则传入的中文没法翻译，英文可以！！！
     msg = quote(msg.decode('gbk').encode('utf-8'))
     youdao.get_translation(msg)
