#3 sum equal to 0
class Solution:
	def threeSum(self, nums):
		triplet=[]
		nums.sort()
		length=len(nums)
		for i in range(length-2):

			if i>0 and nums[i]==nums[i-1]:continue
			l,r =i+1, length-1
			while l<r:
				total = nums[i]+nums[l]+nums[r]
				if total<0:
					l+=1
				elif total>0:
					r-=1
				else:
					triplet.append((nums[i],nums[l],nums[r]))
					#if next number on the left or right is equal to previous number
					#move either l or r forward so no duplicate numbers will be considered
					while l<r and nums[l]==nums[l+1]:
						l+=1
					while l<r and nums[r]==nums[r-1]:
						r-=1
					l+=1
					r-=1
		return triplet

	def threeSum196(self, nums):
		from collections import defaultdict
		#bisect is a binary search module
		import bisect
		ans = []
		#initialize a dictionary store int type
		counter = defaultdict(int)
		for num in nums:
			counter[num] += 1
		nums = sorted(counter)
		print(counter)
		print(nums)
		for i, a in enumerate(nums):   # a < b < c, first fix a, then find b, then find c
			two_sum = 0 - a
			left = bisect.bisect_left(nums, two_sum - nums[-1], i + 1)   # the lower bound of b
			right = bisect.bisect_right(nums, two_sum // 2, left)        # the higher bound of b
			for b in nums[left:right]:
				c = two_sum - b
				if c in counter and c > b:
					ans.append([a, b, c])     # three different elements
			if counter[a] >= 2:
				c = 0 - 2*a
				if c in counter and c != a:
					ans.append([a, a, c])     # two different elements
				if counter[a] >= 3:
					if a*3 == 0:
						ans.append([a, a, a])
		return ans

a = [-1,0,0,1,2,-1,-4,0]
print(Solution().threeSum(a))
print(Solution().threeSum196(a))


