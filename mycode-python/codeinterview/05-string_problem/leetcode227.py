class Solution(object):
    def calculate(self, s):
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign in "-+":
                    stack.append(num if sign=='+' else -num)
                elif sign in "*/":
                    top = stack.pop()
                    stack.append(top*num if sign =='*' else top/num)
                sign = s[i]
                num = 0
        return sum(stack)
if __name__ == "__main__":
    s = Solution()
    print s.calculate('14-3/2')