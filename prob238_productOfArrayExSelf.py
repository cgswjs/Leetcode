class Solution:
	def productExceptSelf(self,nums):
		totalProduct = 1
		for num in nums:
			totalProduct*=num
			print(totalProduct)

		for i in range(len(nums)):
			nums[i]=int(totalProduct/nums[i])

		return nums


	#need to solve it without division
	def productExceptSelfNoDiv(self,nums):
		#left pointer
		left=1
		#right pointer
		right = len(nums)
		#initialize output list
		output = []
		#loop over all elements in list nums
		for i in range(0,right):
			output.append(left)
			left=left*nums[i]

		left = 1
		#reverse loop over the list nums
		for i in range(right-1,-1,-1):
			output[i]=output[i]*left
			left = left*nums[i]

		return output

	def productExceptSelfSimple(self,nums):
		res = [1]*len(nums)
		lprod =1
		rprod =1
		for i in range(len(nums)):
			res[i]*=lprod
			lprod*=nums[i]
			res[~i]*=rprod
			rprod*=nums[~i]
		
		return res

nums = [1,2,3,4]
# print(Solution().productExceptSelf(nums))
print(Solution().productExceptSelfNoDiv(nums))
print(Solution().productExceptSelfSimple(nums))