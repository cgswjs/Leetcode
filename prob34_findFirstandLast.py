class Solution:
	def searchRange(self,nums,target):
		def search(lo,hi):
			#if numbers from lo to hi are all target, return that section of nums list
			if nums[lo]==target==nums[hi]:
				return [lo,hi]
			#otherwise, if only one side is equal to target or target is in side the range of lo to hi
			#recursively call search to divide nums[lo:hi] into two sections
			if nums[lo]<=target<=nums[hi]:
				#update mid for each recursive call
				mid=(lo+hi)//2
				#l is left side indices and r is right side indices
				l,r=search(lo,mid),search(mid+1,hi)
				#if there is -1 in l+r that means no target was found on either side, return the side wihtout -1
				#otherwise, target was found through the left to right side, so return l[0] to r[1]
				return max(l,r) if -1 in l+r else [l[0],r[1]]
			return [-1,-1]
		return search(0,len(nums)-1)

	#2 binary searches
	def searchRange2(self,nums,target):
		def search(n):
			#this is a helper function that implements binary search to find the start index of target in nums
			lo,hi=0,len(nums)
			while lo<hi:
				mid=(lo+hi)//2
				if nums[mid]>=n:
					hi=mid
				else:
					lo=mid+1
			return lo
		lo = search(target)
		#if target is not in nums, search(target+1) will break when lo=hi where num[hi] is the number after target
		return [lo,search(target+1)-1] if target in nums[lo:lo+1] else [-1,-1]

a=[1,2,3,3,3,3,3,3,3,5,7,9,10]
print(Solution().searchRange2(a,3))