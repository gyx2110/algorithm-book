#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip().lower()
    n = int(sys.stdin.readline().strip())
    l,r=0,0
    ans = 0
    num = 0
    while l<len(s) and r<len(s):
        if num<n:
            num+=ord(s[r])-ord('a')+1
            r+=1
        elif num==n:
            num-=ord(s[l])-ord('a')+1
            ans = max(ans,r-l)
            l+=1
        elif num>n:
            num-=ord(s[l])-ord('a')+1
            l+=1
    print ans
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = map(int, line.split())
    #     for v in values:
    #         ans += v
    # print ans