class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue,res = [],[]
        for i in range(len(nums)):
            #当前元素比队尾元素大时 弹出
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            # i - queue[0] == k 最大值已经过期
            if queue and i - queue[0] == k:
                queue.pop(0)
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
if __name__ == "__main__":
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)