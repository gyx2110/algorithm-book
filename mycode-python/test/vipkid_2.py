#coding=utf-8
import sys

if __name__ == "__main__":
    num = map(int,sys.stdin.readline().strip())
    res = 0
    while num:
        num = num & (num-1)
        res+=1
    print res