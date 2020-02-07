class Solution:
	def minSubArrayLenOn(self,s,nums):
		total = left = 0
		result = len(nums)+1
		for right,n in enumerate(nums):
			total += n
			while total>=s:
				result = min(result, right-left +1)
				total -= nums[left]
				left +=1
		return result if result <= len(nums) else 0

	def minSubArrayLenONlogN(self,s,nums):
		result = len(nums)+1
		#enumerate(nums[1:],1) the second 1 after comma makes idx start from 1
		for idx, n in enumerate(nums[1:],1):
			#change nums to a list that holds inclusive sum of previous numbers to current at each element
			nums[idx]=nums[idx-1]+n
		left = 0
		#use binary search
		for right,n in enumerate(nums):
			if n>=s:
				left=self.find_left(left,right,nums,s,n)
				result = min(result,right-left +1)
		return result if result<=len(nums) else 0

	def find_left(self,left,right,nums,target,n):
		while left<right:
			mid = (left+right)//2
			if n-nums[mid]>=target:
				left = mid +1
			else:
				right = mid
		return left




nums=[1,2,3,4,5]
s=11
print(Solution().minSubArrayLenOn(s,nums))
print(Solution().minSubArrayLenONlogN(s,nums))