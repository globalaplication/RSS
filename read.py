#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

class rss(object):
    def __init__(self, url="http://www.haberturk.com/rss/spor.xml"):
        self.news, self.liste, self.url = {}, [], url
    def source(self):
        s=urllib.request.urlopen(self.url)
        return s.read().splitlines()
    def read(self, tag="<title>"):
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and j.find("CDATA") > -1:
                j = j.replace("[","")
                j = j[j.find("!CDATA")+len("!CDATA"):].split("]]")[0]
                self.liste.append(j)
    def get(self, x=0):
        tags = ["<title>", "<description>", "<pubDate>"]
        for j in tags:
            self.read(j)
        y = int( (len(self.liste)+1)/3-1 )
        z = int( len(self.liste) ) -1
        for index in range(x, y+1):
            self.news[index] = {"title":self.liste[index],
            "description":self.liste[y+index], 
            "test":self.liste[z-y+index]}
        return self.news


beta = rss()

print (beta.get())
