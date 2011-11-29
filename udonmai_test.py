#!/usr/bin/python
#-*- coding: utf-8 -*-

import allfiles
import update

if __name__=="__main__":
	path="/home/icys/桌面/wxPython/douban/奶茶"
	list = allfiles.file_list(path)
	mnames = list.listout(0)
	
	for name in mnames:
		music = update.update(name)
		music.search()




