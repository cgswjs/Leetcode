class Solution:
	def merge(self, intervals):
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



a=[[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(a))









