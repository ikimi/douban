# -*- coding:utf-8 -*-
import eyeD3
import re
import urllib

mp3_file = '成全.mp3'

tag = eyeD3.Tag()
tag.link(mp3_file)
print tag.getArtist()
print tag.getAlbum()
print tag.getTitle()
print tag.getImages()
#tag.removeImages()
#tag.encoding = '\x01'
#url = 'http://img1.douban.com/spic/s2891922.jpg'
#path = 'temp.jpg'
#data = urllib.urlopen(url).read()
#f = file(path,"wb")
#f.write(data)
#f.close()
#tag.addImage(3,path,u"")
#tag.update()
