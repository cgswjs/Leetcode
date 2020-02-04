class Solution:
	#traditional two pointers for two sum
	def twoSum2Pointers(self,numbers,target):
		l,r=0,len(numbers)-1
		while l<r:
			s=numbers[l]+numbers[r]
			if s==target:
				return list((l+1,r+1))
			elif s<target:
				l+=1
			else:
				r-=1
		return []		

	#dictionary keep the subtarget in a dictionary corresponding to each num
	def twoSumDict(self,number,target):
		dic={}
		for i,num in enumerate(numbers):
			if target-num in dic:
				return [dic[target-num]+1,i+1]
			dic[num]=i

	#binary search the subtarget
	def twoSumBs(self,numbers,target):
		for i in range(len(numbers)):
			l,r=i+1,len(numbers)-1
			tmp = target-numbers[i]
			while l<=r:
				mid=l+(r-l)//2
				if numbers[mid]==tmp:
					return [i+1,mid+1]
				elif number[mid]<tmp:
					l=mid+1
				else:
					r=mid-1



a=[1,1,2,7,11,15,18]
print(Solution().twoSum2Pointers(a,29))