#!/usr/bin/python
#-*- coding: utf-8 -*-

import allfiles
import update

if __name__=="__main__":
	path="/home/udonmai/桌面/douban_u"
	list = allfiles.file_list(path)
	mnames = list.listout(0)
	
	for name in mnames:
		music = update.update(name[1])
		music.search()




