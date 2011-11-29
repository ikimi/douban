# -*- coding: utf-8 -*-
import threading
import time
import update
from Queue import Queue

# -*- 类接受两个参数 
# -*- name 在信号量队列中的编号
# -*- queue 信号量队列

class customer(threading.Thread):
	Data = []
	def __init__(self,t_name,queue,data):
		threading.Thread.__init__(self,name =t_name)
		self.data = queue
		self.name = t_name
		self.Data = data
	def run(self):
		time.sleep(14)
	#	update.update()
		print self.name
		print self.Data[0] + '/' +self.Data[1] + '.mp3'
		self.data.get()

# -*- 接受两个参数	
# -*- queue 信号量队列	
# -*- num 总的信息数量

class producer(threading.Thread):
	mnames = []
	def __init__(self,queue,num,mnames):
		threading.Thread.__init__(self)
		self.num = num
		self.data = queue
		self.mnames = mnames
	def run(self):
		i = 0
		while i<self.num :
			n = i%self.data.maxsize
			self.data.put(n)
			#创建一个新进程
			c = customer(n,self.data,self.mnames[i])
			c.start()
			i+=1
			time.sleep(1)
					

#def main():
#	queue = Queue(maxsize=5)
#	p = producer(queue,10)
#	p.start()
#	p.join()

#if __name__ == '__main__':
#	main()
