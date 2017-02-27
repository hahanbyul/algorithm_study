#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:01:14 2017

@author: hanbyulkim
"""

class Tiling:
    def __init__(self, n):
        self.cache = [-1 for _ in range(n)]
    
    def compute(self, n):
        if self.cache[n-1] != -1: 
            return self.cache[n]
        
        if n <= 1: return 1
        if n == 2: return 2
        
        ret = self.compute(n - 3) + 2*self.compute(n - 2)
        self.cache[n-1] = ret
        return ret

def main():
    global cache
    N = 7
    t = Tiling(N)
    print(t.compute(N))    

if __name__ == '__main__':
    main()