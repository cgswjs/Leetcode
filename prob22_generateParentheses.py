class Solution:
	def generateParenthesisDP(self,n):
		dp=[[] for i in range(n+1)]
		dp[0].append('')
		for i in range(n+1):
			for j in range(i):
				#since when i=0 and j=0, for loop won't be excuted, dp[0]=['']
				#after that, dp[i] will be equal to each element in dp[j]+all the element in dp[i-j-1]
				dp[i]+=['('+x+')'+y for x in dp[j] for y in dp[i-j-1]]
				#the dp matrix will grow and the last element in dp list will be the answer
		return dp[n]

	def generateParenthesis1(self,n,open=0):
		if n>0<=open:
			return ['('+p for p in self.generateParenthesis1(n-1,open+1)]+\
				   [')'+p for p in self.generateParenthesis1(n,open-1)]
		return[')'*open]*(not n)

	def generateParenthesisStack(self,n):
		#res list that stores the results
		res = []
		#initialize stack
		s = [("(",1,0)]
		#as long as s exists
		while s:
			#pop the last in item from the stack
			x,l,r = s.pop()
			#if the left is smaller than the right or either left or right greater than n
			if l-r<0 or l>n or r>n:
				#keep popping from the stack
				continue
			#if l and r are equal to n
			if l==n and r==n:
				#add just popped x to the result
				res.append(x)
			#keep push ( and ) until l and r are equal to 3
			s.append((x+"(",l+1,r))
			s.append((x+")",l,r+1))
		return res

print(Solution().generateParenthesisDP(3))
print(Solution().generateParenthesis1(3))
print(Solution().generateParenthesisStack(3))
