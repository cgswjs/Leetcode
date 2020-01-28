def reverseInteger(num):
	# 58ms
	# when num<0 true, index is 1 so -1 is used
	# when num<0 false, index is 0 so 1 picked
	sign = [1,-1][num <0]
	rst = sign*int(str(abs(num))[::-1])
	if rst>pow(2,31)-1 or rst<-pow(2,31):
		return 0
	else:
		return rst



def revInt1(x):
	# 48ms
	if x==None:
            return 0
	else:
		if x>=0:
			rx = str(x)[::-1]
			i = 0
			while rx[i]==0:
				i+=1
			rxf = int(rx[i:])

		else:
			rx = str(0-x)[::-1]
			i = 0
			while rx[i]==0:
				i+=1
			rxf = 0-int(rx[i:])     
		return 0 if -pow(2,31)>rxf or rxf>pow(2,31)-1 else rxf 

def revInt2(num):
	# 44ms
	n = int(str(abs(num))[::-1])
	return 0 if num == 0 else ((num>0)-(num<0)) * n * (n < 2**31)  *(n>-2**31-1)


def revInt3(num):
	# 44ms
	rs = str(x)[::-1]
	if rs.endswith('-'):
		# [:-1] exclude the last digit
		rs = '-' + rs[:-1]

	return 0 if int(rs) > 2147483647 or int(rs) < -2147483648 else int(rs)

print(reverseInteger(-234100000))
print(revInt1(123040))
print(revInt2(103))