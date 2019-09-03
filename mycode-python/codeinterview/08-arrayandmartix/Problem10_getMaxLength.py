class MaxLength:
    @classmethod
    def get_max_length(cls,arr, num):
        length = len(arr)
        if length == 0:
            return 0
        left = 0
        right = 0
        sum = 0
        max_len = 0
        while right < length:
            sum += arr[right]
            if sum == num:
                max_len = max(max_len,right-left+1)
                sum -= arr[left]
                left += 1
            elif sum > num:
                sum -= arr[left]
                left += 1
            right += 1
        return max_len
if __name__ == "__main__":
    nums = [3,1,2,1,3]
    k = 4
    print MaxLength.get_max_length(nums,k)