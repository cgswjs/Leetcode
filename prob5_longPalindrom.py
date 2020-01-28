#expane from a center letter for odd palindrom or a group of center letter for even palindrome
#O(n^2)
class Palindrome:
	def __init__(self,s):
		self.s = s

	def longestPalindrome(self):
		#two situation even and odd palindrom
		#exapand judgement
		palindrome=""

		for i in range(len(self.s)):
			#check odd
			len1 = len(self.getlongestpalindrome(self.s,i,i))
			if len1>len(palindrome):
				palindrome = self.getlongestpalindrome(self.s,i,i)

			#check even
			len2 = len(self.getlongestpalindrome(self.s,i,i+1))
			if len2>len(palindrome):
				palindrome = self.getlongestpalindrome(self.s,i,i+1)

		return palindrome

	def getlongestpalindrome(self,s,l,r):
		#as long as l not smaller than left boundary and r not exceed right boundary
		while l>=0 and r<len(s) and s[l]==s[r]:
			l -=1
			r +=1

		return s[l+1:r]



# #Manacher Algorithm O(n)
# class Palindrome:
# 	def __init__(self,s):
# 		self.s = s
	










s = "abcbasdasdaads"
pal = Palindrome(s)
print(pal.longestPalindrome())
