#input string s and pattern p 
#recursion
def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


#DP top down
class SolutionDPTD(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


#DP bottom up
class SolutionDPBU(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

#20ms recursion solution
    def isMatch(s,p):
        mem = {}
        def match(i,j):
            if(i,j) in mem:
                return mem([i,j])
            if j == len(p):
                res=i==len(s)
            else:
                first_match=i!=len(s) and p[j] in {'.',s[i]}
                if j<len(p)-1 and p[j+1]=='*':
                    res = match(i,j+2) or (first_match and match(i+1,j))
                else:
                    res = first_match and match(i+1,j+1)

            mem[(i,j)] = res
            return res
        return match(0,0)


s="abdb"
p="c*abdbc*"

print(isMatch(s,p))

#24ms DP
def isMatch(s,p):
    rows = 1+len(s)
    cols = 1+len(p)
    arr = [[False for i in range(cols)] for j in range(rows)]
    arr[0][0]=True

    i=1
    while i<cols:
        if i<cols-1 and p[i]=="*":
            i=i+1
            for j in range(rows):
                if arr[j][i-2]:
                    arr[j][i]=True
                elif j>0 and arr[j-1][i] and (p[i-2]=="." or p[i-2]==s[j-1]):
                    arr[j][i]=True
            i+=1
        else:
            for j in range(rows):
                if j>0 and arr[j-1][i-1] and (p[i-1]=="." or p[i-1]==s[j-1]):
                    arr[j][i]=True
            i+=1
    return arr[rows-1][cols-1]