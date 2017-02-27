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
        if n <= 1: return 1
        if n == 2: return 2
        
        return self.compute(n - 3) + 2*self.compute(n - 2)

def main():
    global cache
    N = 10
    t = Tiling(N)
    print(t.compute(N))    

if __name__ == '__main__':
    main()