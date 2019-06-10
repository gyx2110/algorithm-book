class Solution(object):
    def longestConsecutive(self, nums):
        map = {}
        res = 0
        for num in nums:
            if num not in map:
                lb = map.get(num-1,0)
                rb = map.get(num+1,0)
                length = rb + lb + 1
                res = max(res,length)
                map[num] = length
                map[num - lb] = length
                map[num + rb] = length
        return res
if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])