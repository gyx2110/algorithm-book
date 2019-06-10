class Solution(object):
    def maxProduct(self, nums):
        if not nums or len(nums) == 0:
            return 0
        _min = _max = res = nums[0]
        for num in nums[1:]:
            minEnd = _min*num
            maxEnd = _max*num
            _min = min(min(minEnd,maxEnd),num)
            _max = max(max(minEnd,maxEnd),num)
            res = max(res,_max)
        return res
if __name__ == "__main__":
    s = Solution()
    print s.maxProduct([0,-3,-5])