#!/usr/bin/python
#-*- coding: utf-8 -*-

import allfiles

if __name__=="__main__":
	path="/home/udonmai/桌面/douban_u"
	list = allfiles.file_list(path)
	mnames = list.listout(0)
	
	for name in mnames:
		print name[1]




