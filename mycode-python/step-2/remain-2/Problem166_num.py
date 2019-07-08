class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        res = []
        res.append('-' if (numerator > 0) ^ (denominator > 0) else '')
        num = abs(numerator)
        den = abs(denominator)

        res.append(num / den)
        num%=den
        if num ==0:
            return ''.join(map(str,res))
        
        res.append('.')
        pos = {}
        pos[num] = len(res)
        while num:
            num *=10
            res.append(num / den)
            num %= den

            if pos.get(num,-1) != -1:
                index = pos.get(num)
                res.insert(index,'(')
                res.append(')')
                break
            else:
                pos[num] = len(res)
        return ''.join(map(str,res))
if __name__ == "__main__":
    s = Solution()
    print s.fractionToDecimal(2,0)