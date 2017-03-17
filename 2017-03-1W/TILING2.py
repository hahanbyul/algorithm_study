#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:01:14 2017

@author: hanbyulkim
"""
import sys
rl = lambda: sys.stdin.readline()
MAX_VAL = 1000000007

class Tiling:
    def __init__(self, n):
        self.cache = [-1 for _ in range(n)]

    def compute(self, n):
        if self.cache[n-1] != -1: 
            return self.cache[n-1]
        
        if n <= 1: return 1
        if n == 2: return 2
        
        ret = self.compute(n - 3) + 2*self.compute(n - 2) # 여기서 mod 해야 함
        self.cache[n-1] = ret
        return ret

def main():
    C = int(rl())
    
    for _ in range(C):
        n = int(rl())
        t = Tiling(n)
        print(t.compute(n) % MAX_VAL)    

if __name__ == '__main__':
    main()
