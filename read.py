#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

class rss(object):
    def __init__(self):
        self.news = {}
    def source(self, url="http://www.haberturk.com/rss/spor.xml"):
        s=urllib.request.urlopen(url)
        return s.read().splitlines()
    def read(self, tag="<title>"):
        next, test = 0, {}
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and j.find("CDATA") > -1:
                next = next + 1
                j = j.replace("[","")
                j = j[j.find("!CDATA")+len("!CDATA"):].split("]]")[0]
                test[next] = {tag[1:-1]:j}
                self.news.update( test )
   
    def get(self):
        tags = ["<title>", "<description>", "<pubDate>"]
        for j in tags:
            self.read(j)
        return self.news


beta = rss()

print (beta.get())
