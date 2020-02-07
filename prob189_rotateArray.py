class Solution:
	def rotate(self,nums,k):
		for i in range(k):
			nums.insert(0,nums[-1])
			nums.pop()
		return nums

	def rotateFast(self,nums,k):
		n=len(nums)
		k=k%n
		if len(nums)==1 or k==0:
			return nums
		nums=nums[-k:]+nums[:n-k]

nums=[1,2,3,4,5,6,7]
k=3

import timeit
start=timeit.timeit()
print(Solution().rotate(nums,k))
# print(Solution().rotateFast(nums,k))
end = timeit.timeit()
print("Time: {}".format(abs(start-end)))

