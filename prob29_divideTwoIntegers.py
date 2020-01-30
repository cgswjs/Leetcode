class Solution:
	def divide(self,dividend, divisor):
		sign=((dividend<0)!=(divisor<0))
		dividend=left=abs(dividend)
		divisor=div=abs(divisor)
		Q=1
		ans=0
		while left>=divisor:
			#keep subtracting div to reach maximum left that is smaller than div
			left-=div
			#add Q to answer
			ans+=Q
			#make Q double
			Q+=Q
			#make div double
			div+=div
			#check if left is still larger than doubled div,if yes keep going through the while loop
			#if not, reset div and Q to original and check while loop again
			if left<div:
				div=divisor
				Q=1

		#check if there is a negative sign 
		if sign:
			#if yes, return -ans if it's larger than MIN_INT
			return max(-ans,-2147483648)
		else:
			#if no, return the smaller number comparing ans and MAX_INT
			return min(ans,2147483648)


divident=13
divisor=-3
print(Solution().divide(divident,divisor))

