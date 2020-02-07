class Solution:
	def rotatePythonic(self,matrix):
		#use * to unpack matrix and zip to pack them
		#zip returns all elements in each column one by ones
		#since zip is a iterating function, [:] is needed to assign each iteration to corresponding element in matrix
		matrix[:] = zip(*matrix[::-1])
		return matrix

	def rotateCleaner(self,matrix):
		n=len(matrix)
		for i in range(n//2):
			for j in range(n-n//2):
				matrix[i][j],matrix[~j][i],matrix[~i][~j],matrix[j][~i]= \
				matrix[~j][i],matrix[~i][~j],matrix[j][~i],matrix[i][j]

		return matrix

	def rotateComprehension(self,matrix):
		#same idea as the first pythonic solution but using comprehension
		matrix[:]=[[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
		return matrix






matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print(Solution().rotatePythonic(matrix))
# print(Solution().rotateComprehension(matrix))
# print(Solution().rotateCleaner(matrix))

