#remove dupilicates without using extra memory
a = [1,1,1,2,3,4,5,5,5,5,6,6,6,8,8,8,9]
def removeDuplicates(nums):
	l = 0#pointer that records unique element in array
	if len(nums) == 0: return l
	for i in range(len(nums)):
		if nums[l]<nums[i]:
			l += 1
			nums[l]=nums[i]
		print(i,l)
	
removeDuplicates(a)