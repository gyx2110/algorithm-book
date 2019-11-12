class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        tmp_res = []
        self.dfs(n,1,k,res,tmp_res)
        return res
    def dfs(self,target,cur,k,res,tmp_res):
        if target==0 and k==0:
            res.append(tmp_res[::])
        else:
            i=cur
            while i<10:
                if target-i>=0 and k>0:
                    tmp_res.append(i)
                    self.dfs(target-i,i+1,k-1,res,tmp_res)
                    tmp_res.pop()
                i+=1
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum3(3,9)


# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]