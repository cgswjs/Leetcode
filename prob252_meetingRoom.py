class Solution:
	#76 ms
	def canAttendMeeting(self,intervals):
		intervals.sort(key=lambda x:x[0])
		for i in range(len(intervals)-1):
			if intervals[i][1]>intervals[i+1][0]:
				return False
		return True

	def canAttendMeetings(self,intervals):
		intervals.sort(key=lambda x:x[0])
		res=[]
		for i in intervals:
			#use a res list to keep track of valid meeting time
			if not res or res[-1][-1]<=i[0]:
				res.append(i)
			else:
				return False
		return True

a=[[7,10],[2,4]]
print(Solution().canAttendMeeting(a))
