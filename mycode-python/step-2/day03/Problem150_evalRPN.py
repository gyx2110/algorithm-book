class Solution(object):
    def evalRPN(self, tokens):
        s = []
        for c in tokens:
            if c.isdigit() or ('-' in c and len(c)>1):
                s.append(int(c))
            else:
                b = s.pop()
                a = s.pop()
                if c == '+':
                    s.append(a+b)
                if c == '-':
                    s.append(a-b)
                if c == '*':
                    s.append(a*b)
                if c == '/':
                    s.append(a/b)
        return s[0]
if __name__ == "__main__":
    s = Solution()
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])    