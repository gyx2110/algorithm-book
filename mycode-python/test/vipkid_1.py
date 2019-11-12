#coding=utf-8
import sys

if __name__ == "__main__":
    nums = map(int,sys.stdin.readline().strip().split(','))
    nums.sort()
    l,r=0,len(nums)-1
    res=0
    while l<r:
        if l==0 or nums[l] != nums[l-1]:
            if nums[l]+nums[r]==0:
                l+=1
                r-=1
                res+=1
            elif nums[l]+nums[r]>0:
                r-=1
            elif nums[l]+nums[r]<0:
                l+=1
        else:
            l+=1
    print res
        