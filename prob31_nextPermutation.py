class Solution:
	def nextPermutation(self,nums):
		i=j=len(nums)-1
		#going through every number in this list nums
		#if left number if greater than current num that means the lexicographical order is right
		while i>0 and nums[i-1]>=nums[i]:
			i-=1
		#if i==0, this means that all numbers in this list nums are in lexicographical order, return reversed nums
		if i==0:
			return nums[::-1]

		#if nums is not in lexicographical order, it will be the first position that left number is smaller
		#find the previous position using k
		k=i-1
		#starting from right end again and compare with k
		while nums[j]<=nums[k]:
			j-=1
		nums[k],nums[j]=nums[j],nums[k]

		#reverse the right side after k point
		l,r = k+1,len(nums)-1
		while l<r:
			nums[l],nums[r]=nums[r],nums[l]
			l+=1
			r-=1
		return nums

nums=[1,2,3]
print(Solution().nextPermutation(nums))
print(Solution().nextPermutation(nums))
print(Solution().nextPermutation(nums))
print(Solution().nextPermutation(nums))
print(Solution().nextPermutation(nums))