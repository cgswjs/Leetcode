class Solution:
	def __init__(self):
		self.letter={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
		self.letter2 = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

	def letterCombinations(self,digits:str):
		cmb = [''] if digits else []
		for d in digits:
			cmb=[p+q for p in cmb for q in self.letter[d]]
			
		return cmb

	def letterCombinationsTuple(self,digits:str):
		res = [''] if digits else []
		for i in digits:
			res=[pre+cur for pre in res for cur in self.letter2[int(i)]]
		return res

a='234'
mapping = Solution()
print(mapping.letterCombinations(a))
print(mapping.letterCombinationsTuple(a))