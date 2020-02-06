class Solution:
	def subsets(self,nums):
		res=[[]]
		if not nums:return res
		slow=0
		while slow <len(nums):
			fast=slow
			while fast<len(nums):
				if nums[slow]==nums[fast]:
					res.append([nums[slow]])
				else:
					res.append([nums[slow],nums[fast]])
				fast+=1
			slow+=1
		res.append(nums)
		return res

	def subsetsSimple(self,nums):
		res=[[]]
		for num in nums:
			#loop over res and concatenate element in res with new number
			#[]+[1]=[1],res+=[1]=[[],[1]] and keep going
			res+=[i + [num] for i in res]
		return res

	#DFS
	def __init__(self):
		self.res=[]

	def subsetsDFS(self,nums,path=[]):
		#add current path to res
		self.res.append(path)
		#input next number to subsetsDFS and add current number to path
		for i in range(len(nums)):
			self.subsetsDFS(nums[i+1:],path+[nums[i]])
		return self.res

nums = [1,2,3]
print(Solution().subsets(nums))
print(Solution().subsetsSimple(nums))
print(Solution().subsetsDFS(nums))