#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

class rss(object):
    def __init__(self):
        self.news = {}
        self.liste = []
    def source(self, url="http://www.haberturk.com/rss/spor.xml"):
        s=urllib.request.urlopen(url)
        return s.read().splitlines()
    def read(self, tag="<title>"):
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and j.find("CDATA") > -1:
                j = j.replace("[","")
                j = j[j.find("!CDATA")+len("!CDATA"):].split("]]")[0]
                self.liste.append(j)
    def get(self):
        tags = ["<title>", "<description>", "<pubDate>"]
        for j in tags:
            self.read(j)

        x = 0
        y = int( (len(self.liste)+1)/3-1 )
        z = int( len(self.liste) ) -1

        for index in range(x, y+1):
            print (index, y+index+1, z-y+index )
            self.news[index] = {"title":self.liste[index],
            "description":self.liste[y+index+1], 
            "test":self.liste[z-y+index]}

        return x, y, z


beta = rss()

print (beta.get())
