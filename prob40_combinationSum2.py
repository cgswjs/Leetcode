class Solution:
	#DP solution
	def combinationSum2DP(self,candidates,target):
		candidates.sort()
		dp = [set() for i in range(target+1)]
		dp[0].add(())
		for num in candidates:
			for t in range(target,num-1,-1):
				for prev in dp[t-num]:
					#to create tuple type for single element, add a comma after the element
					dp[t].add(prev+(num,))
		return list(dp[-1])

	#recursive solution
	def combinationSum2Rec(self,candidates,target):
		candidates.sort()
		result=[]
		self.combine_sum_2(candidates,0,[],result,target)
		return result

	def combine_sum_2(self,nums,start,path,result,target):
		if not target:
			result.append(path)
			return

		for i in range(start,len(nums)):
			if i>start and nums[i]==nums[i-1]:
				continue
			if nums[i]>target:
				break
			self.combine_sum_2(nums,i+1,path+[nums[i]],result,target-nums[i])
		

a=[10,1,2,7,6,1,5]
print(Solution().combinationSum2DP(a,8))
print(Solution().combinationSum2Rec(a,8))