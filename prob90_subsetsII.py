class Solution:
	def subsetsWithDup(self,nums):
		if not nums:
			return []
		nums.sort()
		res,cur = [[]],[]
		for i in range(len(nums)):
			#if greater than 0 and current number equal to previous number
			#use elements in res to add new number will create duplicates
			if i>0 and nums[i]==nums[i-1]:
				cur = [item+[nums[i]] for item in cur]
			else:
				#if not, use elements in res to add new number
				cur = [item+[nums[i]] for item in res]
			res+=cur
		return res

	def subsetsWithDupDFS(self,nums):
		res=[]
		nums.sort()
		self.dfs(nums,0,[],res)
		return res

	def dfs(self,nums,index,path,res):
		res.append(path)
		for i in range(index,len(nums)):
			if i>index and nums[i]==nums[i-1]:
				continue
			self.dfs(nums,i+1,path+[nums[i]],res)


a=[4,4,4,1,2]
print(Solution().subsetsWithDup(a))
print(Solution().subsetsWithDupDFS(a))

