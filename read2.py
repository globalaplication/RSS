#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
class beta(object):
    def __init__(self, url="https://www.aspor.com.tr/rss/galatasaray.xml"):
        self.news, self.title, self.description, self.pubDate, self.url = {}, [],[], [], url
    def source(self):
        s=urllib.request.urlopen(self.url)
        return s.read().splitlines()
    def get(self, tag="<title>"):
        for j in self.source():
            j = j.decode('utf-8', 'backslashreplace')
            if j.find(tag) > -1 and j.find("CDATA") > -1:
                j = j.replace("[","")
                j = j[j.find("!CDATA")+len("!CDATA"):].split("]]")[0]
                if (tag == "<title>"):
                    self.title.append(j)
                elif (tag == "<description>"):
                    self.description.append(j)
                elif (tag == "<pubDate>"):
                    self.pubDate.append(j)
            elif j.find(tag) > -1 and j.find("CDATA") is -1:
                j = j[j.find(tag)+len(tag):-len(tag)-1]
                if (tag == "<title>"):
                    self.title.append(j)
                elif (tag == "<description>"):
                    self.description.append(j)
                elif (tag == "<pubDate>"):
                    self.pubDate.append(j)
        return zip(self.title, 
            self.description, 
                   self.pubDate)
    def read(self):
        tags = ["<title>", "<description>", "<pubDate>"]
        for j in tags:
            self.get(j)
        for string in zip(self.title, self.description, self.pubDate):
            print ("{}\n{}\n{}\n".format(string[0], string[1], string[2]))
        return 

rss = beta()
print( rss.read() )
 
