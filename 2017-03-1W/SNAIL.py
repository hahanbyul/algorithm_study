#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:52:23 2017

@author: hanbyulkim
"""
import sys
rl = lambda: sys.stdin.readline()

class SNAIL:
    def __init__(self, m, n, rain_prob):
        self.m = m
        self.n = n
        self.rain_prob = rain_prob
        
        self.cache = [[-1 for _ in range(2*m+1)] for _ in range(m)]
    
    def start(self):
        #return self.climb(self.m, 0) / 2**self.m
        return self.climb_in_rainy_season(0, 0)
        
    def climb(self, days, climbed):
        print("days: %d, climbed: %d" % (days, climbed))
        # base condition
        if days == 0:
            return 1 if climbed >= self.n else 0

        if self.cache[self.m - days][climbed] != -1: 
            return self.cache[self.m - days][climbed]
        
        ret = self.climb(days - 1, climbed + 2) + self.climb(days - 1, climbed + 1)
        return ret

    def climb_in_rainy_season(self, days, climbed):
        if days == self.m:
            return 1.0 if climbed >= self.n else 0.0

        cached = self.cache[days-1][climbed] 
        if cached != -1:
            print("cached")
            return cached

        prob_sunny = 1.0 - self.rain_prob
        prob_rainy = self.rain_prob
        ret = prob_sunny * self.climb_in_rainy_season(days + 1, climbed + 1) + prob_rainy * self.climb_in_rainy_season(days + 1, climbed + 2)
        self.cache[days-1][climbed] = ret
        return ret
        
def main():
    snail = SNAIL(m=10, n=2, rain_prob=0.75)
    print(snail.cache)
    prob = snail.start()
    print(prob)
    
if __name__ == '__main__':
    main()
