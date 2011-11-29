import time
#import thread
import threading
from Queue import Queue
#def timer(no,interval):
#	cnt = 0
#	while cnt<10:
#		print 'Thread:(%d) Time:%s\n'%(no,time.ctime())
#		time.sleep(interval)
#		cnt+=1
#	thread.exit_thread()
#
#def test():
#	thread.start_new_thread(timer,(1,1))
#	thread.start_new_thread(timer,(2,2))

#class timer(threading.Thread):
#	def __init__(self,num,interval):
#		threading.Thread.__init__(self)
#		self.num = num
#		self.interval = interval
#		self.thread_stop = False
#	
#	def run(self):
#		while not self.thread_stop:
#			print 'Thread Object(%d),Time:%s\n' %(self.num,time.ctime())
#			time.sleep(self.interval)
#
#	def stop(self):
#		self.thread_stop = True
#
#def test():
#	thread1 = timer(1,1)
#	thread2 = timer(2,2)
#	thread1.setDaemon(True)
#	thread1.start()
#	thread2.start()
#	time.sleep(10)
#	thread1.stop()
#	thread2.stop()
#	print "main process stoped!"
#	time.sleep(5)
#	thread1.stop()
#	print "main process stoped!"
#	return 

if __name__=='__main__':
	test()
	time.sleep(20)
