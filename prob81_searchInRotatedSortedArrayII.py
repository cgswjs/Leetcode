class Solution:
	def search(self,nums,target):
		l,r = 0,len(nums)-1
		while l<=r:
			mid=(l+r)//2
			if nums[mid]==target:
				return True
			if num[l]<=nums[mid]:
				if nums[l]<=target<nums[mid]:
					#check if left number is same as mid
					#move the mid to most left if updating right boundary
					while nums[mid-1]==nums[mid]:
						mid-=1
					r=mid-1
				else:
					#check if right number is the same as mid
					#move mid to the most right if updating left boundary
					while nums[mid+1]==nums[mid]:
						mid+=1
					l=mid+1
			else:
				if nums[mid]<target<=nums[r]:
					while nums[mid+1]==nums[mid]:
						mid+=1
					l=mid+1
				else:
					while nums[mid-1]==nums[mid]:
						mid-=1
					r=mid-1
		return False

nums=[2,5,6,0,0,00,0,0,0,0,0,0,0,0,0,0,1,2]
target=0

import timeit
start=timeit.timeit()
print(Solution().search(nums,target))
end=timeit.timeit()
print("This takes {}".format(abs(start-end)))