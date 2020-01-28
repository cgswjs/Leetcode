class Solution:
	def threeSumClosest(self,nums,target):
		nums.sort()
		length=len(nums)
		diff = float('Inf')
		for i in range(length-2):
			l,r = i+1,length-1
			while l<r:
				total = nums[i]+nums[l]+nums[r]
				curDiff = abs(total-target)
				if total==target:
					return total
					
				if curDiff<diff:
					result = total
					diff=curDiff
				if total<target:
					l+=1
				elif total>target:
					r-=1
				

		return result



a = [1,1,1,0]
print(Solution().threeSumClosest(a,-100))
print(abs(102)<float('Inf'))
