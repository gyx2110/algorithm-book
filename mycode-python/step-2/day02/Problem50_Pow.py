# class Solution(object):
    # def myPowCore(self, x, n):
    #     if n<0:
    #         x = 1/x
    #         n = -n
    #     if n==0:
    #         return 1.0
    #     elif n==1:
    #         return x
    #     else:
    #         if n%2==0:
    #             return self.myPowCore(x, n/2)**2
    #         else:
    #             return self.myPowCore(x, n-1)*x
    # def myPow(self, x, n):
    #     return self.myPowCore(x,n)
    # def myPow(self, x, n):
class Solution(object):
    def myPow(self, x, n):
        if n<0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n%2:
                res *=x
                n = n-1
            else:
                x *=x
                n/=2
        return res
if __name__ == "__main__":
    s = Solution()
    # print s.myPow(2,1024)
    print s.myPow(2,10)