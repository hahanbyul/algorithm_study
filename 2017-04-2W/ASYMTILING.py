#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:01:14 2017

@author: hanbyulkim
"""
MAX_VAL = 1000000007


class Asymtiling:
    def __init__(self):
        self.cache = dict()
        self.cache[0] = 1
        self.cache[1] = 1
        self.cache[2] = 2

        self.cache_sym = dict()
        self.cache_sym[0] = 1
        self.cache_sym[1] = 1
        self.cache_sym[2] = 2
        self.cache_sym[3] = 1

    def compute(self, n):
        if self.cache.get(n, False):
            return self.cache[n]
        
        ret = (self.compute(n - 1) + self.compute(n - 2)) % MAX_VAL # 여기서 mod 해야 함
        self.cache[n] = ret
        return ret

    def compute_sym(self, n):
        if self.cache_sym.get(n, False):
            return self.cache_sym[n]

        ret = (self.compute_sym(n - 4) + self.compute_sym(n - 2)) % MAX_VAL
        self.cache_sym[n] = ret
        return ret

    def compute_asym(self, n):
        all_tiles = self.compute(n)
        sym_tiles = self.compute_sym(n)
        # print(f'all: {all_tiles}, sym: {sym_tiles}')
        return all_tiles - sym_tiles if all_tiles >= sym_tiles else (all_tiles - sym_tiles) + MAX_VAL


def main():
    C = int(input())
    for _ in range(C):
        n = int(input())
        t = Asymtiling()
        print(t.compute_asym(n))    

if __name__ == '__main__':
    main()
