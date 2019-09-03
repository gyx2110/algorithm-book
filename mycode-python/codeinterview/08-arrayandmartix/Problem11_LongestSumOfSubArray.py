class LongestSumOfSubArray:
    @classmethod
    def get_longest_sum(cls, nums, k):
        if len(nums) == 0:
            return 0
        sum = 0
        max_len = 0
        map = dict()
        map[0] = -1
        i = 0
        while i < len(nums):
            sum += nums[i]
            if (sum - k) in map:
                j = map.get(sum - k)
                max_len = max(max_len,i-j)
            if sum not in map:
                map[sum] = i
            i += 1
        return max_len
if __name__ == "__main__":
    #map{0: -1, 2: 0, 3: 1, 4: 3, 5: 4}
    nums = [2,1,-1,2,1]
    k = 3
    print LongestSumOfSubArray.get_longest_sum(nums,k)