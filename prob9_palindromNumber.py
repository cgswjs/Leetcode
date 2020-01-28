#runtime 76ms 27%
num = 10
def isPalindrom(num):
	num = str(num)
	if len(num)==1:return True
	if num[0]=="-":return False
	l=0
	r=len(num)-1
	count = False
	while l<=r:
		if num[l]==num[r]:
			l+=1
			r-=1
			count=True
		else:
			count=False
			break
	return count

print(isPalindrom(num))	


#24ms solution
def isPalindromFast(num):
	if num<0:return False
	num=str(num)
	return num==num[::-1]

print(isPalindromFast(num))