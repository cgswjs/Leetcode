class Solution:
	def maxSubArrayLen(self,nums,k):
		ans,acc = 0,0
		#initialize a dictionary, since start from 0, final answer needs to be add 1
		mp = {0:-1}
		#loop over all elements in nums
		for i in range(len(nums)):
			#keep adding numbers
			acc+=nums[i]
			#keep tracking index of current sum
			if acc not in mp:
				mp[acc]=i
			#if current sum-k is equal to any previous sum or 0, return
			if acc-k in mp:
				ans = max(ans,i-mp[acc-k])
		return ans,mp

k=8
nums=[0,1,2,5,1,1,1,0]
print(Solution().maxSubArrayLen(nums,k))