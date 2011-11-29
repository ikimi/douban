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
	#	print filename
	#返回歌曲信息
	def search(self):
		self.url = self.url + "?" + "q=" + self.filename + "&alt=json"
		req = urllib2.Request(self.url)
		fd = urllib2.urlopen(req)
		data = fd.read()
		entries = json.loads(data)
		author = 'author'
		Data ={}
		#满足符合的歌曲总数
		Len = json.dumps(entries['opensearch:totalResults'],ensure_ascii=False)	
		Sum = int(Len[8:len(Len)-2])
		#如果没有查询到结果
		if Sum == 0:
			print "Not Found!"
		#如果仅存在一条结果
		elif Sum == 1:
			entry = entries['entry'][0]
			if author in entry:
				Data['author'] = json.dumps(entry['author'][0]['name'],ensure_ascii = False)
				Data['author'] = Data['author'][8:len(Data['author'])-2]
			else:
				Data['author'] = ''
			Data['Album'] = json.dumps(entry['title'],ensure_ascii = False)
			Data['Album'] = Data['Album'][8:len(Data['Album'])-2] 
			Data['img'] = json.dumps(entry['link'][2],ensure_ascii = False)
			Data['img'] = Data['img'][28:len(Data['img'])]
		#如果存在多条结果
		else:
			i = 1
			for entry in entries['entry']:
				if author in entry:
					#Data['author'] = json.dumps(entry['author'][0]['name'],ensure_ascii = False) #专辑名
					print i,json.dumps(entry['author'][0]['name'],ensure_ascii = False)
				else:
					#Data['author'] = ''
					print ''
				#Data['img'] = json.dumps(entry['link'][2],ensure_ascii = False)
				print json.dumps(entry['link'][2],ensure_ascii = False)		#专辑封面url
				print json.dumps(entry['title'],ensure_ascii = False)
				#Data['Album'] = json.dumps(entry['title'],ensure_ascii=False)  	#歌手名
				i+=1
			id = input("please input the id:\n")
			#根据用户输入更新文件信息
			result = entries['entry'][id-1]
			if author in result:
				Data['author'] = json.dumps(result['author'][0]['name'],ensure_ascii = False)
				Data['author'] = Data['author'][8:len(Data['author'])-2]	#歌手名
			#	print Data['author']
			Data['img'] = json.dumps(result['link'][2],ensure_ascii = False)	#专辑封面url
			Data['img'] = Data['img'][28:len(Data['img'])-2]
			#print Data['img']
			Data['Album'] = json.dumps(result['title'],ensure_ascii = False)	#专辑名
			Data['Album'] = Data['Album'][8:len(Data['Album'])-2]
			#print Data['Album']

		self.refresh(Data)
	
	#更新歌曲信息
	def refresh(self,data):
		print data['author']
		print data['Album']
		print data['img']
		tag = eyeD3.Tag()
		print self.filename
		tag.link(self.filename)
		tag.removeImages()
		tag.encoding = '\x01'
		#设置歌手
		tag.setArtist(data['author'])
		print tag.getArtist()
		#设置专辑
		tag.setAlbum(data['Album'])
		print tag.getAlbum()
		img = urllib.urlopen(data['img']).read()
		temp = file('temp.jpg','wb')
		temp.write(img)
		temp.close()
		tag.addImage(3,'temp.jpg',u"")
		tag.update()	
