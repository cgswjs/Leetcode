class Solution:
	#this solution will have duplicates 
	def fourSum(self,nums,target):
		if not nums or not target:return []
		self.res = []
		path = []
		self.DFS(sorted(nums),path,target)
		return self.res

	def DFS(self,nums,path,target):
		if target<0: return
		elif target == 0:
			self.res.append(path)
		else:
			for i,x in enumerate(nums):
				if x<= target:
					self.DFS(nums[i:],path+[x],target-x)
			return

	#reduce 4 sum to 2 sum O(n^2)
	def fourSum3(self,nums,target):
		res=[]
		if nums is None:return res
		nums.sort()
		for i in range(len(nums)-3):
			if i==0 or nums[i]!=nums[i-1]:
				for j in range(i+1,len(nums)-2):
					if j==i+1 or nums[j]!=nums[j-1]:
						l,r=j+1,len(nums)-1
						subtar=target-nums[i]-nums[j]
						while l<r:
							if nums[l]+nums[r]==subtar:
								res.append((nums[i],nums[j],nums[l],nums[r]))
								while l<r and nums[l]==nums[l+1]:
									l+=1
								while l<r and nums[r]==nums[r-1]:
									r-=1
								l+=1
								r-=1
							elif nums[l]+nums[r]>subtar:
								r-=1
							else:
								l+=1
		return res



a=[1,1,1,1,1,2,2,3,4,5]

print(Solution().fourSum3(a,12))