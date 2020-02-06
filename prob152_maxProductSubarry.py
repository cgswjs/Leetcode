class Solution:
	def maxProduct(self,nums):
		comp = nums[::-1]
		for i in range(1,len(nums)):
			nums[i]*=nums[i-1]
			comp[i]*=comp[i-1]
		return max(nums+comp)

a=[2,3,-4,2,-6]
print(Solution().maxProduct(a))
