import sys

class a:
	def __init__(self,name):
		self.name = name
		self.show(1)
	def show(self,n):
		print self.name
		self.n = n
		if self.n<3:
			self.show(self.n+1)
	def s(self):
		print self.n

if __name__ =='__main__':
	temp = a('a')
	temp.s()
