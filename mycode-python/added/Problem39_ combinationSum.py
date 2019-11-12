class Solution(object):
    def combinationSum(self, nums, target):
        res = []
        lst = []
        self.dfs(nums,target,0,res,lst)
        return res
    def dfs(self,nums,target,k,res,tmp_res):
        if target==0:
            # append a copy
            res.append(tmp_res[::])
        else:
            i=k
            while i<len(nums):
                if target-nums[i]>=0:
                    tmp_res.append(nums[i])
                    self.dfs(nums,target-nums[i],i,res,tmp_res)
                    tmp_res.pop()
                i+=1
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7],9)


# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]