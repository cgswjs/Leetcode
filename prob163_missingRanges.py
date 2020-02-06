class Solution:
	def findMissingRanges(self,nums,lower,upper):
		res = []
		nums.append(upper+1)
		pre = lower-1
		for i in nums:
			if i-pre==2:
				res.append(str(i-1))
			elif i-2>pre:
				res.append(str(pre+1)+"->"+str(i-1))
			pre = i
		return res,nums

nums=[0,1,3,50,75]
lower = 0
upper = 99
print(Solution().findMissingRanges(nums,lower,upper))
