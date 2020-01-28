class Solution:
	def intToRoman(self, num: int) -> str:
		values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
		res =""
		for n,v in zip(numerals, values):
			res+=(num//v)*n
			num%=v
		return res

	#fastest 24ms
	def intToRomanFast(self,num:int) -> str:
		M=["","M","MM","MMM"]
		C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
		X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
		I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
		return M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[num%10]


a=4
print(Solution().intToRoman(a))

