from heapq import *
class Solution:
	def __init__(self):
		self.stream=[]
		self.heaps = [],[]

	def addNum(self,num):
		self.stream.append(num)

	def findMedian(self):
		if len(self.stream)%2:
			self.median = self.stream[(len(self.stream)+1)//2-1]
		elif not len(self.stream)%2:
			self.median = (self.stream[len(self.stream)//2-1]+self.stream[len(self.stream)//2])/2
		return self.median

	def addNumHeap(self,num):
		small,large = self.heaps
		heappush(small,-heappushpop(large,num))
		if len(large)<len(small):
			heappush(large,-heappop(small))

	def findMedianHeap(self):
		small,large = self.heaps
		if len(large)>len(small):
			return float(large[0])
		return (large[0]-small[0])/2.0



s = Solution()
s.addNum(1)
s.addNum(2)
s.addNum(3)
s.addNum(4)
s.addNum(5)
median = s.findMedian()
# print(median)

s.addNumHeap(1)
s.addNumHeap(2)
s.addNumHeap(3)
s.addNumHeap(5)
s.addNumHeap(7)
# print(s.findMedianHeap())

