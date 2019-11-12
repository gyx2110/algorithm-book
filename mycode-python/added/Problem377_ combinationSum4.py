class Solution(object):
    def combinationSum4(self, nums, target):
        if target==0:
            return 1
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,len(dp)):
            for j in range(0,len(nums)):
                if i-nums[j]>=0:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]

    def combinationSum4(self, nums, target):
        if target==0:
            return 1
        res = 0
        for num in nums:
            if target-num>=0:
                res+=self.combinationSum4(nums,target-num)
        return res
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum4([1,50],2000)
