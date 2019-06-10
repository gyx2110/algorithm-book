class Solution(object):

    def __init__(self, nums):
        self.origin = nums
    def reset(self):
        return self.origin
    def shuffle(self):
        new_list = self.origin[:]
        k = len(new_list)
        import random
        for i in range(k,1,-1):
            t = random.randint(0,i-1)
            tmp = new_list[t]
            new_list[t] = new_list[i-1]
            new_list[i-1] = tmp
        return new_list
if __name__ == "__main__":
    s = Solution([1,2,3])
    print s.shuffle()
    print s.shuffle()
    print s.shuffle()
    print s.shuffle()
    print s.reset()