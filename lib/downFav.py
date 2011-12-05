#! 
# -*- coding:utf-8 -*-
 
from BeautifulSoup import BeautifulSoup
from eyeD3 import *
import urllib,urllib2,cookielib,re
 
def handle(s):
    return s.replace("&lt;","<").replace("&gt;",">").replace("\\","")
   
def fhandle(s):
    return s.replace("/","and").replace(" ","")

#修改tag信息
def modify(self, s1, s2, s3, img_path):
	tag = eyeD3.Tag()
	if not tag.link(self):
		tag.header.setVersion(eyeD3.ID3_V2_3)
	tag.encoding = '\x01'
	
	tag.setTile(s1)
	tag.setArtist(s2)
	tag.setAlbum(s3)
	
	img = urllib.urlopen(img_path).read()
	temp = file('temp.jpg','wb')
	temp.write(img)
	temp.close()
	tag.addImage(3,'temp.jpg',u"")
	tag.update()
 
def get(myurl,cookie):
    url2="http://douban.fm/j/mine/playlist?type=n&h=&channel=0&context=channel:0|subject_id:%d"
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req=urllib2.Request(myurl)
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    req.add_header('Cookie',cookie)
    content=urllib2.urlopen(req).read()
    soup=BeautifulSoup(str(content))
    soup=soup.find("div", { "id" : "record_viewer" })
    for div in soup.findAll("div", { "class" : "info_wrapper" }):
		div=div.find("div",{ "class" : "song_info" })
		a=div.contents[1]
		p1,p2,p3=div.contents[3].findAll("p")
		print a["href"]+"\nsong:"+handle(p1.string)+"\nsinger:"+handle(p2.string)+"\nalbum:"+handle(p3.a.string)
		p=re.compile(r'(\d+)')
		m=p.search(a["href"])
		num=int(m.groups()[0])
		url3=url2%num
		print url3
		mark=False
		#获取专辑封面
		sub_path = a["href"]#专辑链接
		req2 = urllib2.Request(sub_path)
		content2 = urllib2.urlopen(req2).read()
		soup2 = BeautifulSoup(str(content2))
		soup2 = soup2.find("div", {"id" : "mainpic"})
		img_pathc = soup2.contents[1]
		img_path = img_pathc["href"]

		try:
			for j in range(100):
				content=urllib2.urlopen(url3).read()
				c=eval(content)
				c=c['song']
				for i in c:
					if unicode(str(i['title']),'utf-8')==handle(p1.string):
						#tag = eyeD3.Tag()
						local = "../Incoming/" + fhandle(handle(p1.string)) + "-" + fhandle(handle(p2.string)) + ".mp3"
						urllib.urlretrieve(i['url'].replace('\\',''), local)
						modify(local, fhandle(handle(p1.string)), fhandle(handle(p2.string)), fhandle(handle(p3.string)), img_path)
						mark=True
						break
				if mark:
					break
			if mark:
				print "succeed!\n"
			else: print "fail!\n"
		except Exception as e:
			print e.message
 
def main():
    url="http://douban.fm/mine?start=%d&type=liked"
    cookie=raw_input('cookie:')
    print "you should enter the pages you want to download"
    page0=int(raw_input('page from:'))
    page1=int(raw_input('page to:'))
    for i in range(page1-page0+1):
        get(url%((i+page0-1)*15),cookie)
 
if __name__ == "__main__":
    main()
