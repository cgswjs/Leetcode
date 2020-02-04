#this problem is the same as prob56 except insert a new list
#Use problem 56 script to merge lists after insert newInterval
class Solution:
	#intervals contains non overlapping lists
	#newInterval is a new list insert to intervals, merge if neccessary
	def insert(self,intervals,newInterval):
		intervals.append(newInterval)
		intervals.sort(key=lambda x:x[0])
		out=[]
		for i in intervals:
			#if out is not empyt and current list is overlapping with previous list, merge current list with previous list
			if out and i[0]<=out[-1][1]:
				out[-1][1]=max(out[-1][1],i[1])
			#push in the current list if out is empty or current list is not able to be merged with previous one
			else:
				out.append(i)
		return out

a=[[1,3],[6,9]]
b=[2,5]
print(Solution().insert(a,b))