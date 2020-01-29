class Solution:
	def removeDuplicates(self,nums):
		fast=1
		slow=0

		while fast<=len(nums)-1:
			if nums[fast]==nums[slow]:
				nums.pop(fast)
			else:
				slow=fast
				fast+=1
		return len(nums)

	def removeDuplicates60(self,nums):
		i=0
		n=len(nums)
		last=None
		for  num in nums:
			if num != last:
				nums[i]=num
				i+=1
			last=num
		return i

	def removeDuplicatesSimple(self,nums):
		index=0
		for num in nums:
			#keep comparing each num with previous non-duplicated number
			#Because the list is sorted, any number before current index can be considered
			#Non-duplicated
			if num != nums[index]:
				index+=1
				nums[index]=num
		#since the first element nums[0] was used to compare and didn't count for the length
		#return index+1
		return index+1

	def removeDuplicates(self,nums):
		l = 0#pointer that records unique element in array
		if len(nums) == 0: return l
		for i in range(len(nums)):
			if nums[l]<nums[i]:
				l += 1
				nums[l]=nums[i]
			print(i,l)

a=[1,1,2]
print(Solution().removeDuplicates(a))
