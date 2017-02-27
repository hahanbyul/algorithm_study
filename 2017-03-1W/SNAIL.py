#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:52:23 2017

@author: hanbyulkim
"""
class SNAIL:
    def __init__(self, m, n, rain_prob):
        self.m = m
        self.n = n
        self.rain_prob = rain_prob
        
        self.cache = [[-1 for _ in range(n)] for _ in range(m)]
    
    def start(self):
        return self.climb(self.m, 0) / 2**self.m
        
    def climb(self, days, climbed):
        if self.cache[m - days][climbed] != -1: return self.cache[m - days][climbed]
        if days == 0:
            return 1 if climbed >= self.n else 0
        
        ret = self.climb(days - 1, climbed + 2) + self.climb(days - 1, climbed + 1)
        return ret

    def climb_in_rainy_season(self, days, climbed):
        if days == 0:
            return 1 if climbed >= self.n else 0
        
        return (1 - self.rain_prob)*self.climb(days - 1, climbed + 2) + self.rain_prob*self.climb(days - 1, climbed + 1)
        
def main():
    snail = SNAIL(m=10, n=2, rain_prob=0.75)
    print(snail.cache)
    prob = snail.start()
    print(prob)
    
if __name__ == '__main__':
    main()