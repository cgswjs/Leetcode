A = [100,4,200,1,3,2,5,7,9,10,8,11,12,13]
#set is O(n)
a = set(A)
print(a)

#O(n)
def longestConSeq(l):
	best = 0
	for x in a:
	#check previous num of x 
		xp=x-1
		#if xp is not in a that means x is the smallest num for this sequence
		if xp not in a:
		#update count of this sequence
			xc = 1
			#move pointer to the next number of this sequence
			y = x+1
			#as long as the next number of this sequence is in the set
			#this sequence is keep growing
			while y in a:
				y=y+1
				xc+=1

			#update the longest consecutive sequence	
			best = max(best,xc)

	return f'length of {best}'

best = longestConSeq(a);
print('The longest consecutive sequence has {}'.format(best))
