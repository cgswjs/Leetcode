#Given a data stream input of non-negative intergers a1,a2,a3....an
#Summarize the numbers seen so far as a list of disjoint intervals
#Explanation: keep input elements [1,3,7,2,6]
#when input 1, interval is [1,1]
#when input 3, since 3 and 1 are not continuous, we have two intervals [1,1],[3,3]
#when input 7, same reason, we have three intervals [1,1],[3,3],[7,7]
#when input 2, since 2 is between 1 and 3, we merge it to [1,3],[7,7]
#when input 6, same reason, we have [1,3],[6,7]
#We can use binary search tree since python doesn't have treemap
#Or brute force as follow
class Solution:
	def __init__(self):
		#initialize a set seen, two dictionary for start and end to store input numbers
		self.seen = set()
		self.start,self.end = dict(),dict()

	def addNum(self,val):
		#if input number has already been input before, don't do anything
		if val in self.seen:
			return
		#otherwise, add it to seen
		self.seen.add(val)
		#interval will be the input number itself at first
		interval=[val,val]
		#check if input number+1 or input number-1 is in start or end
		if val+1 in self.start.keys():
			interval[1]=self.start[val+1]
			#pop out val+1 and its value
			self.start.pop(val+1)
		if val-1 in self.end.keys():
			interval[0]=self.end[val-1]
			#pop out val-1 key and its value
			self.end.pop(val-1)
		#push new interval into start and end dictionaries
		self.start[interval[0]]=interval[1]
		self.end[interval[1]]=interval[0]

	def getIntervals(self):
		#.items() method output dictionary as tuple which has a format (key,value)
		return sorted(self.start.items())


res = Solution()
res.addNum(1)
print(res.getIntervals())
res.addNum(3)
print(res.getIntervals())
res.addNum(7)
print(res.getIntervals())
res.addNum(2)
print(res.getIntervals())
res.addNum(6)
print(res.getIntervals())
res.addNum(4)
print(res.getIntervals())
res.addNum(9)
print(res.getIntervals())
