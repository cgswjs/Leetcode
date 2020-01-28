class Solution:
	def longestCommonPrefix(self,strs)->str:
		if not strs:
			return ""
		shortest = min(strs,key=len)
		for i, ch in enumerate(shortest):
			for other in strs:
				if other[i]!=ch:
					return shortest[:i] 
		return shortest

	def longestCommonPrefixFast(self,strs):
		if not strs:return ''
		s1 = min(strs)
		s2 = max(strs)

		for i,c in enumerate(s1):
			if c!=s2[i]:
				return s1[:i]
		return s1

a=["aaa","dacecar","cac"]
print(Solution().longestCommonPrefix(a))
print(Solution().longestCommonPrefixFast(a))