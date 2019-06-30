class Solution(object):
    def countAndSay(self, n):
        if n == 0:
            return ''
        res = '1'
        while n-1>0:
            cur = ''
            n-=1
            i=0
            while i<len(res):
            # for i in range(len(res)): 这种写法不行
                count=1
                while i+1<len(res) and res[i]==res[i+1]:
                    count+=1
                    i+=1
                cur+=str(count)+res[i]
                i+=1
            res=cur
        return res
if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(3)