#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
class beta(object):
    def __init__(self, url="http://www.haberturk.com/rss/spor.xml"):
        self.news, self.title, self.description, self.pubDate, self.url = {}, [],[], [], url
    def gettag(self, string, tag="<title>"):
        if string.find("CDATA") is -1:
            return 0
        if string.find("CDATA") > -1:
            endtag = string.find("{}/{}".format(tag[0:1], tag[1:]))
            return string[string.find(tag)+len(tag):endtag].replace("<![CDATA[",
            "").replace("]]>","")
    def source(self):
        s=urllib.request.urlopen(self.url)
        return s.read().splitlines()
    def get(self, tag="<title>"):
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and self.gettag(j) is not 0:
                print(self.gettag(j))
                
rss = beta()
rss.get()

