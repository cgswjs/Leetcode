import timeit
class Solution:	
	def isValidSudokuSetSimple(self, board):
		#initiate a set to store visited location and value
		big = set()
		for i in range(0,9):
			for j in range(0,9):
				if board[i][j]!='.':
					cur = board[i][j]
					#use i/3, j/3 to find sub box in sudoku since one number can only appear once in a 3x3 box in a 9x9 sudoku
					if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
						return False
					#add current value and location into set if not added earlier
					big.add((i,cur))
					big.add((cur,j))
					big.add((i/3,j/3,cur))
		return True


a=[["5","3",".",".","7",".",".",".","."],
  ["6",".",".","7","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","4"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

b=[[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]


start2=timeit.timeit()
print(Solution().isValidSudokuSetSimple(a))
end2 = timeit.timeit()
print("Time for leetcode method: {}".format(abs(start2-end2)))

