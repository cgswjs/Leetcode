class Solution:
	def minMeetingRooms(self,intervals):
		#sort start and end times
		starts = sorted(i[0] for i in intervals)
		ends = sorted(i[1] for i in intervals)
		#initialize a index e
		e=0
		#initial room 0
		numRooms = available = 0
		#chek start and end time, if end time is smaller than start time, available room increase by one
		for start in starts:
			while ends[e]<=start:
				available+=1
				e+=1

			if available:
				available-=1
			else:
				numRooms+=1
		return numRooms


a=[[1,5],[8,9],[8,11],[8,12]]
print(Solution().minMeetingRooms(a))