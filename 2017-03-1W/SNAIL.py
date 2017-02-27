#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:52:23 2017

@author: hanbyulkim
"""
class SNAIL:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    
    def start(self):
        return self.climb(self.m, 0) / 2**self.m
        
    def climb(self, days, climbed):
        if days == 0:
            return 1 if climbed >= self.n else 0
        
        return self.climb(days - 1, climbed + 2) + self.climb(days - 1, climbed + 1)

def main():
    snail = SNAIL(m=10, n=2)
    prob = snail.start()
    print(prob)
    
if __name__ == '__main__':
    main()