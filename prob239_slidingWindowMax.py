class Solution:
	#brute force
	#brute force did a lot of duplicated calculation since overlapping issue
	#if we add the next number to current window and remove the first number from previous window, it will be faster 
	def maxSlidingWindow(self,nums,k):
		if k==0:return []
		if k==1:return nums
		res=[]
		for i in range(0,len(nums)-k+1):
			res.append(max(nums[i:i+k]))
		return res

	#priority queue solution O(N)
	def maxSlidingWindowQueue(self,nums,k):
		from collections import deque
		d = deque()
		out = []
		for i,n in enumerate(nums):
			#when d is true, compare current number with previuos max
			while d and nums[d[-1]]<n:
				d.pop()
			#i, makes i a iterable list type instead of a int type
			d+=i,
			#when i arrives the next window and current max number is out of left bound of k, pop the previous max
			if d[0]==i-k:
				d.popleft()
			#when i is greater or equal to the right bound of k, keep adding the first element in prioritory queue to result list
			if i>=k-1:
				#same as before
				out += nums[d[0]],
		return out

	#heap solution O(NlogN)
	def maxSlidingWindowHeap(self,nums,k):
		import heapq as h
		if k==0: return []
		heap=[]
		for i in range(k):
			h.heappush(heap,(nums[i]*-1,i))
		result,start,end = [],0,k-1
		while end<len(nums):
			x,idx = self.get_next_max(heap,start)
			result.append(x)
			h.heappush(heap,(x*-1,idx))
			start,end = start+1,end+1
			if end<len(nums):
				h.heappush(heap,(nums[end]*-1,end))
		return result

	def get_next_max(self,heap,start):
		import heapq as h
		while True:
			x,idx = h.heappop(heap)
			if idx>= start:
				return x*-1,idx


nums=[1,3,-1,4,5,3,6,7]
print(Solution().maxSlidingWindow(nums,3))
print(Solution().maxSlidingWindowQueue(nums,3))
print(Solution().maxSlidingWindowHeap(nums,3))