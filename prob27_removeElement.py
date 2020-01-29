class Solution:
	def removeElement(self,nums,val):
		pointer=0
		while pointer<=len(nums)-1:
			if nums[pointer]==val:
				nums.pop(pointer)
			else:
				pointer+=1
		return nums

a=[3,2,2,3]
print(Solution().removeElement(a,3))