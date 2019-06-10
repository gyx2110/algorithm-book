class Solution(object):
    def minWindow(self, s, t):
        ls = len(s)
        lt = len(t)
        if not s or not t or ls<lt:
            return ''
        min_size = ls + 1
        l = r = 0
        start=0
        end = ls-1
        map = {}
        #对t中的字符计数
        for c in t:
            map[c] = map.get(c,0)+1
        match = 0
        while r<ls:
            map[s[r]] = map.get(s[r],0)-1
            #如果当前遇到的字符在map中出现过，则匹配数+1
            match = match+1 if map[s[r]]>=0  else match
            #当匹配完成时窗口左滑
            if match==lt:
                #尝试左滑窗口 对之前遇到的字符出窗口
                while map[s[l]]<0:
                    map[s[l]]+=1
                    l+=1
                if min_size > r - l + 1:
                    min_size = r - l +1
                    start = l
                    end = r
            r+=1
        return '' if min_size>ls else s[start:end+1]