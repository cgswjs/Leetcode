class Solution:
	# faster than 47.39%
	def lengthOfLongestSubstring(self,s):
		#s is a input string
		temp = []#a list to keep track on visited element
		leng = 0 #current longest substring length

		for x in s:
			if x in temp:
				temp = temp[temp.index(x)+1:]

			temp.append(x)
			leng = max(leng,len(temp))

		return leng

	#faster than 97%
	def lengthOfLongestSubstring(self,s):
		no_repeat_string = ""
		max_count = 0
		for char in s:
			if char in no_repeat_string:
				max_count = max_count if len(no_repeat_string)< max_count else len(no_repeat_string)
				index_repeat = no_repeat_string.index(char)
				no_repeat_string = no_repeat_string[index_repeat+1:]
			else:
				no_repeat_string = no_repeat_string+char

		return max_count if len(no_repeat_string)<max_count else len(no_repeat_string)