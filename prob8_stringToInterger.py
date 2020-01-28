#discard all empty space
#if the first non empty space is numerical value convert it to int until the non-numerical value after that
#if the first non empty space is not numerical return 0
#if converted number is greater than 2**31-1 or smaller than -2**31 return INT_MAX OR INT_MIN
import timeit

def atoiConvert(str1):
	test="-1234567890"
	number=""
	count=0
	maxVal = 2**31-1
	minVal = -(2**31)
	while count<len(str1):
		if str1[count]!=" ":
			number+=str1[count]			
		count+=1
	if number[0] not in test:
		return 0
	else:
		sign = [1,-1][number[0]=="-"]
		if number[0]=="-":
			number=number[1:]
		if number[0]=="0":
			count=0
			while count<len(number):
				if number[count]=="0":
					count+=1
				else:
					break
		number = number[count:]
	
			
		count1=0
		count2=1
		while count2<len(number):
			if number[count2] in test:
				count2+=1
			else:
				break
			
		outval = sign*int(number[count1:count2])
		if minVal<outval<maxVal:
			return outval
		elif outval<minVal:
			return minVal
		elif outval>maxVal:
			return maxVal

#use Regular Expression
def myAtoi(str1) -> int:
	import re
	str1 = str1.strip()
	str1 = re.findall('(^[\+\-0]*\d+)\D*',str1)
	try:
		result = int(''.join(str1))
		MAX_INT = pow(2,31)-1
		MIN_INT = -pow(2,31)
		if result > MAX_INT:
			return MAX_INT
		elif result<MIN_INT:
			return MIN_INT
		else:
			return result
	except:
		return 0


str1 = "000000000412as123dfasdf"
start1 = timeit.timeit()
print(atoiConvert(str1))
end1 = timeit.timeit()
print("Time for brute force is {}".format(abs(end1-start1)))
start2 = timeit.timeit()
print(myAtoi(str1))
end2 = timeit.timeit()
print("Time for regular expression is {}".format(abs(end2-start2)))


