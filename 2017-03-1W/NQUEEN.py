#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:19:39 2017

@author: hanbyulkim
"""

class NQueen:
    def __init__(self, N):
        self.answers = []
        self.N = N
        
    def find(self, picked_cols):
        if len(picked_cols) == self.N:
            answers.append([col for col in picked_cols])
            return True
        
        current_row = len(picked_cols)
        for i in range(self.N):
            if i in picked_cols: continue
            
            if check_diag(picked_cols, current_row, i):
                picked_cols.append(i)
                ret = find(picked_cols)
                picked_cols.pop()
            else:
                ret = False
            return ret

    def check_diag(self, picked_cols, row, col):
        return True
        
def main():
    NQueen(2)
    
if __name__ == '__main__':
    main()
