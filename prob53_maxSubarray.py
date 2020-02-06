class Solution:
	#if previous number is positive we add it to current number and make it the current number
	#if the result is still positive, we keep adding next number to current number until a negative number shows up 
	#keep doing this make sure that positive numbers are added together which result in the largest sum
	def maxSubArray(self,nums):
		for i in range(1,len(nums)):
			if nums[i-1]>0:
				nums[i]+=nums[i-1]
		return max(nums)

	def maxSubArray2(self,nums):
		if not nums:
			return 0
		curSum = maxSum=nums[0]
		for num in nums[1:]:
			curSum = max(num,curSum+num)
			maxSum = max(maxSum,curSum)
		return maxSum

a=[-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(a))