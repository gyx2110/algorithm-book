class Solution(object):
    def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, []
    l,r = 0,len(s)
    while l<r:
        if s[l].isdigit():
            num = 0
            while l<r and s[l].isdigit():
                num = 10*num+ord(s[l])-ord('0')
                l+=1
            l-=1
            res+=num*sign
        elif s[l] in '+-':
            sign = [-1,1][s[l]=='+']
        elif s[l] == '(':
            stack.push(res)
            stack.push(sign)
            res = 0
            sign = 1
        elif s[l] == ')':
            res = res * stack.pop()+stack.pop()
    return res