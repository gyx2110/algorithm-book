class Solution(object):
    map = []
    def rob(self, nums):
        self.map = [-1 for x in range(len(nums))]
        return self.robCore(nums,0)
    def robCore(self,nums,k):
        if k>=len(nums):
            return 0
        if self.map[k]!= -1:
            return self.map[k]
        n = len(nums[k:])
        if n<=2:
            return max(nums[k:])
        a = max(self.robCore(nums,k+2),self.robCore(nums,k+1))
        b = self.robCore(nums,k+2)+nums[k]
        self.map[k] = max(a,b)
        return self.map[k]
if __name__ == "__main__":
    s = Solution()
    print s.rob([2,7,9,3,1])
    