class Solution(object):
    def reverse(self, x):
        bound = 2**31-1
        is_pos = x > 0
        res, right = 0, 0
        while x:
            right = x % 10
            if res > (bound - right)/10
                return 0
            res = 10 * res + right
        return res if is_pos else -res
