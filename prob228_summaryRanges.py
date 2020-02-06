class Solution:
	def summaryRanges(self,nums):
		res=[]
		for n in nums:
			#if res is None or n is not the next number of previous, add a new sub list
			if not res or n>res[-1][-1]+1:
				res+=[],
			#add current number to the last element of the last sub list
			res[-1][1:]=n,
		return ["->".join(map(str,r)) for r in res]

	def summaryRanges2(self,nums):
		begin,res = 0,[]
		strout = lambda b,e:str(b) + "->"+str(e) if b!=e else str(b)
		for i in range(1,len(nums)+1):
			if i==len(nums) or nums[i]-nums[i-1]!=1:
				res.append(strout(nums[begin],nums[i-1]))
				begin = i
		return res

nums = [0,1,2,4,5,7,9,12]
print(Solution().summaryRanges(nums))
print(Solution().summaryRanges2(nums))