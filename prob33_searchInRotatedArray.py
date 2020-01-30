class Solution:
	def search(self,nums,target):
		#left and right boundary
		lo,hi = 0,len(nums)-1
		#using binary search
		while lo<hi:
			mid=(lo+hi)/2
			#nums[0]> target means target on the right side
			#nums[0]>nums[mid] mid+1 is the new left boundary
			#target>nums[mid] means target on right side
			if(nums[0]>target)^(nums[0]>nums[mid])^(target>nums[mid]):
				lo=mid+1
			else:
				hi=mid
		return lo if target in nums[lo:lo+1] else -1

	def binarySearch(self,nums,target):
		l,r=0,len(nums)-1
		while l<=r:
			mid=l+(r-l)//2
			#find target 
			if nums[mid]==target:
				return mid
			#if left side is smaller or equal to mid,update r if target is between left and mid
			#otherwise, update l
			if nums[l]<=nums[mid]:
				if nums[l]<=target<nums[mid]:
					r=mid-1
				else:
					l=mid+1
			else:
				#if target is on the right side
				if nums[mid]<target<=nums[r]:
					l=mid+1
				else:
					r=mid-1
		return -1



		

