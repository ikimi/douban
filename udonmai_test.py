#!/usr/bin/python
#-*- coding: utf-8 -*-

import allfiles

if __name__=="__main__":
	path="/home/udonmai/桌面/douban_u"
	tmp_list = allfiles.all_files(path, 0, 10)
	print tmp_list[9][1]




