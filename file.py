# -*- coding:utf-8 -*-
import os
import update
class file:
	self.filename = {}
	def __init__(self,filename):
		self.filename = filename
	
	def basename(self):
		return os.path.basename(self.filename)


if __name__ == '__main__':
	tmp = file("爱的代价.mp3")
	temp = update.update(tmp.basename())
	temp.search()
