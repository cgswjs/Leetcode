import timeit
class Solution:
	def searchInsert(self, nums, target):
		if target<nums[0]:return 0
		if target>nums[-1]:return len(nums)
		
		pointer=0
		while pointer<len(nums):
			if target<=nums[pointer]:
				break
			pointer+=1
		return pointer

	def searchInsertOneLine(self,nums,target):
		return len([x for x in nums if x<target])

	def searchInsert28(self,nums,target):
		left=0
		right=len(nums)
		while left<right:
			mid = (left+right)//2

			if nums[mid]==target:
				return mid
			elif nums[mid]<target:
				left=mid+1
			else:
				right=mid

		return left

a=[1,3]
start1=timeit.timeit()
print(Solution().searchInsert(a,3))
end1=timeit.timeit()
print("Time for 1: {}".format(abs(start1-end1)))

start2=timeit.timeit()
print(Solution().searchInsertOneLine(a,3))
end2=timeit.timeit()
print("Time for 2: {}".format(abs(start2-end2)))

start3=timeit.timeit()
print(Solution().searchInsertOneLine(a,3))
end3=timeit.timeit()
print("Time for 3: {}".format(abs(start3-end3)))