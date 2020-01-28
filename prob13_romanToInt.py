import re
class Solution:
	def romanToInt(self,s:str) -> int:
		roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
		z = 0
		for i in range(len(s)-1):
			if roman[s[i]]<roman[s[i+1]]:
				z-=roman[s[i]]
			else:
				z+=roman[s[i]]
		return z+roman[s[-1]]

	def romanToIntFast(self, s: str) -> int:
		count = 0
		size = len(s)
		for x in range(size):
			if s[x] == 'I':
				if x<size-1 and s[x+1] in 'VX':
					count-=1
				else:
					count+=1
			elif s[x] == 'X':
				if x<size-1 and s[x+1] in 'LC':
					count-=10
				else:
					count+=10
			elif s[x] == 'C':
				if x<size-1 and s[x+1] in 'DM':
					count-=100
				else:
					count+=100
			elif s[x] == 'V':
				count += 5
			elif s[x] == 'L':
				count += 50
			elif s[x] == 'D':
				count += 500
			elif s[x] == 'M':
				count += 1000
			else:
				return -1
		return count


	def romanToIntFast2(self, s: str) -> int:
		return sum(s.count(r)*v for r,v in [('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000),('IV',-2),('IX',-2),('XL',-20),('XC',-20),('CD',-200),('CM',-200)])  


    # def romanToIntFast3(self, s):
    #     i = 0
    #     dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #     res = 0
    #     while (i < len(s)):
    #         s1 = dict[s[i]]
    #         if i+1 < len(s):
    #             s2 = dict[s[i+1]]
    #             if s1 >= s2:
    #                 res += s1
    #             else:
    #                 res = res + s2 - s1
    #                 i = i + 1
    #         elif i < len(s):
    #             res += s1 
    #         i += 1
    #     return res

rom = "LVIII"
print(Solution().romanToIntFast2(rom))