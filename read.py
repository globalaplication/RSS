#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

class rss(object):
    def source(self, url="http://www.haberturk.com/rss/spor.xml"):
        s=urllib.request.urlopen(url)
        return s.read().splitlines()
    def read(self, tag="<title>"):
        news = {}
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and j.find("CDATA") > -1:
                j = j.replace("[","")
                j = j[j.find("!CDATA")+len("!CDATA"):].split("]]")[0]
                news.update( [ {j:""} ])
        return news

    def get(self):
        tags = ["<title>", "<description>", "<pubDate>"]
        for j in tags:
            print (j)


beta = rss()

print (beta.read("<pubDate>"))
