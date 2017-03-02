#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:33:55 2017

@author: hanbyulkim
"""
import sys
rl = lambda: sys.stdin.readline()

class TriPath:
    def __init__(self, N, board):
        self.N = N
        self.cache = [[-1 for _ in range(N)] for _ in range(N)]
        self.isMaxPath = False
        self.board = board
    
    def path(self, y, x):
        return 0
        
    def path_num(self, y, x):
        if not self.isMaxPath: 
            self.path(0, 0)
            
        if y == self.N - 1: 
            return 1
        
        left  = self.cache[y+1][x]
        right = self.cache[y+1][x+1]
        
        if   left == right: return self.path_num(y+1, x) + self.path_num(y+1, x+1)
        elif left >  right: return self.path_num(y+1, x)
        elif left <  right: return self.path_num(y+1, x+1)

def parse_board(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        board[row][:row+1] = (int(num) for num in rl().split())
    return board

def main():
    #C = int(rl())
    C = 1

    for _ in range(C):
        n = int(rl())
        print(parse_board(n))
    return 0

if __name__ == '__main__':
    main()
