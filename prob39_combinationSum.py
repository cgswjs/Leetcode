#Using DFS
class Solution:
	def combinationSumDFS(self,candidates,target):
		candidates.sort()
		res=[]

		#create a helper DFS function
		def dfs(target, index, path):
			if target<0:
				return
			if target == 0:
				res.append(path)
				return
			for i in range(index, len(candidates)):
				dfs(target-candidates[i],i,path+[candidates[i]])

		dfs(target,0,[])
		return res

	def combinationSumDP(self,candidates,target):
		candidates.sort()
		#this dp is a 3D matrix
		#1st dimension: list represents different cases for different total
		#2nd dimension: dp[s] represents results when total is s
		#3rd dimension: dp[s][j] represents the jth case when total is s
		#initialize a dp matrix
		dp=[[[]]]+[[] for i in range(target)]
		#iterate through all numbers in candidates
		for n in candidates:
			#all cases for total between n to target inclusively
			for s in range(n,target+1):
				li=[l+[n] for l in dp[s-n]]
				dp[s]+=li
		return dp[target]

	def combinationSumBFS(self,candidates,target):
		candidates.sort()
		stack=[(0,0,[])]
		result=[]
		while stack:
			total,start,res = stack.pop()
			if total == target:
				result.append(res)
			for n in range(start,len(candidates)):
				t=total+candidates[n]
				if t>target:
					break
				stack.append((t,n,res+[candidates[n]]))
		return result

a=[1,2,3,4,5,6,7,11,20]
print(Solution().combinationSumDFS(a,18))
print(Solution().combinationSumDP(a,18))