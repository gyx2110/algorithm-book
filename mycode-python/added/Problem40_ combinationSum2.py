class Solution(object):
    def combinationSum2(self, nums, target):
        res = []
        lst = []
        nums.sort()
        self.dfs(nums,target,0,res,lst)
        return res
    def dfs(self,nums,target,k,res,tmp_res):
        if target==0:
            # append a copy
            res.append(tmp_res[::])
        else:
            i=k
            while i<len(nums):
                if i>k and nums[i]==nums[i-1]:
                    i+=1
                    continue
                if target-nums[i]>=0:
                    tmp_res.append(nums[i])
                    self.dfs(nums,target-nums[i],i+1,res,tmp_res)
                    tmp_res.pop()
                i+=1
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5],8)


# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]