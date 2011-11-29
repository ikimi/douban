# -*- coding: utf-8 -*-
import threading
import time
from Queue import Queue

class customer(threading.Thread):
	def __init__(self,t_name,queue):
		threading.Thread.__init__(self,name=t_name)
		self.data=queue
		self.name=t_name
	def run(self):
		time.sleep(6)
		print self.name
		self.data.get()

class producer(threading.Thread):
	def __init__(self,queue,num):
		threading.Thread.__init__(self)
		self.num = num
		self.data = queue
	#	print self.data.maxsize	
	def run(self):
		i = 0
		while i<self.num :
			n = i%5
			self.data.put(n)
			#创建一个新进程
			c = customer(n,self.data)
			c.start()
			i+=1
			time.sleep(1)
					

def main():
	queue = Queue(maxsize=5)
#	print queue.maxsize
	p = producer(queue,10)
	p.start()
	p.join()

if __name__ == '__main__':
	main()
