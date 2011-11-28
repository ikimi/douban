# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys
import json
import eyeD3

class update:
	url = "http://api.douban.com/music/subjects"
	def __init__(self,filename=''):
		self.filename = filename
		print filename
	#返回歌曲信息
	def search(self):
	#	self.url = self.url + "?" + "q=" + self.filename + "&alt=json"
	#	req = urllib2.Request(self.url)
	#	fd = urllib2.urlopen(req)
	#	data = fd.read()
	#	entries = json.loads(data)
	#	author = 'author'
		Data ={}
		#for entry in entries['entry']:
		#	if author in entry:
		#		Data['author'] = json.dumps(entry['author'][0]['name'],ensure_ascii=False) #专辑名
		#	else:
		#		Data['author'] = ''
		#	print json.dumps(entry['title'],ensure_ascii=False)
		#	Data['title'] = json.dumps(entry['title'],ensure_ascii=False)   			#歌手名
		#	print json.dumps(entry['id'],ensure_ascii=False)			#id
		Data['author'] = "刘若英"
		Data['Album'] = "爱的代价"
		self.refresh(Data)
	
	#更新歌曲信息
	def refresh(self,data):
		print data['Album']
		print data['author']
		tag = eyeD3.Tag()
		tag.link(self.filename)
		tag.setAlbum(data['Album'])
		tag.setArtist(data['author'])
		tag.update()	
