class Solution:
	def isValid(self,s):
		stack = []
		check={"]":"[","}":"{",")":"("}
		for char in s:
			if char in check.values():
				stack.append(char)
			elif char in check.keys():
				if stack==[] or check[char]!=stack.pop():
					return False

		return stack==[]
				

a = "(())"
print(Solution().isValid(a))
