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
        
def main():
    NQueen(2)
    
if __name__ == '__main__':
    main()