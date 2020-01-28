import pdb

def zigZagString(l,n):
	#initialize a list that contains designated rows
	zigzag = ['' for x in range(n)]
	# zigzag = [[]]*n
	rows = []
	row = 0 #pointer for rows

	#return original string if there is only 1 row or len(l) rows
	if n==1 or n>=len(l):
		return l

	#for eligible rows, do the zigzag
	for crct in l:
		zigzag[row]+=crct
		if row == 0:
			step = 1
		elif row==n-1:
			step =-1
		row+=step
	
	return ''.join(zigzag)

l="PAYPALISHIRING"
z1 = zigZagString(l,4)
print(z1)

#use for crct in l is faster than using for i in range(len(s))
