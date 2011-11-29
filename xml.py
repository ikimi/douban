# -*- coding:utf-8 -*-
import urllib2
import urllib
import sys

url = "http://api.douban.com/music/subjects?q=爱的代价"
req = urllib2.Request(url)
fd = urllib2.urlopen(req)
data = fd.read()
print data

