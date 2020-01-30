class Solution:
	def strStr(self,haystack,needle):
		import re
		return	re.search(needle,haystack).start() if re.search(needle,haystack) else -1


	def strStr8(self,haystack,needle):
		if haystack=="" and needle=="":
			return 0
		else:
			#find returns the index of first occurence of target needle
			c=haystack.find(needle) if needle in haystack else -1
			return c

	def strStr16(self,haystack,needle):
		if needle in haystack:
			return haystack.index(needle)
		return -1

haystack="This is an apple"
needle='is'
print(Solution().strStr16(haystack,needle))