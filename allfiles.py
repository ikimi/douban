#!/usr/bin/python
#-*- coding: utf-8 -*- 

import os

start = 0#起始位置

def all_files(path, start, end):
	i = start 
	filename = ''
	path_list = []
	flag = True#标识是否有结束位置的设置
	if end == None:
		flag = False

	for root,dirs,files in os.walk(path):
		for filespath in files:
			filename = filespath.partition('.mp3')#分片
			path_list.append([root,filename[0]])
			i += 1
			if flag and i == end:
				return path_list

	return path_list		

