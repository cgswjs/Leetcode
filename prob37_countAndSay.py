class Solution:
	def countAndSayRE1(self,n):
		import re
		s='1'
		for _ in range(n-1):
			s=re.sub(r'(.)\1*',lambda m:str(len(m.group(0)))+m.group(1),s)
		return s

	def coutnAndSayRE2(self,n):
		import re
		s='1'
		for _ in range(n-1):
			s=''.join(str(len(group))+digit for group,digit in re.findall(r'((.)\2*)',s))
		return s

	def countAndSayGroupby(self,n):
		s='1'
		for _ in range(n-1):
			s=''.join(str(len(list(group)))+digit for digit,group in itertools.groupby(s))

	def countAndSaySimple(self,n):
		s='1'
		for i in range(n-1):
			count=1
			temp=[]
			for index in range(1,len(s)):
				if s[index]==s[index-1]:
					count+=1
				else:
					temp.append(str(count))
					temp.append(s[index-1])
					count=1
			temp.append(str(count))
			temp.append(s[-1])
			s=''.join(temp)
		return s

print(Solution().countAndSaySimple(10))