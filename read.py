#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

def source(url="http://www.haberturk.com/rss/spor.xml"):
    s=urllib.request.urlopen(url)
    return s.read().splitlines()

for j in source():
    j = j.decode('utf-8', 'backslashreplace')
    if j.find("<title>") > -1 and j.find("CDATA") > -1:
        print (j)
