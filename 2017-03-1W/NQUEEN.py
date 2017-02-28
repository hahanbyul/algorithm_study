#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:19:39 2017

@author: hanbyulkim
"""

class NQUEEN:
    def __init__(self, N):
        self.answers = []
        self.N = N
        self.find([])
        
    def find(self, picked_cols):
        #print(self.to_board(picked_cols))

        if len(picked_cols) == self.N:
            self.answers.append(self.to_board([col for col in picked_cols]))
            return
        
        current_row = len(picked_cols)
        for i in range(self.N):
            #print("i:", i)

            if i in picked_cols or self.is_diag(picked_cols, i): 
                #print('continue')
                continue
            
            picked_cols.append(i)
            self.find(picked_cols)
            picked_cols.pop()

    def is_diag(self, picked_cols, test_col):
        test_row = len(picked_cols)

        for row, col in enumerate(picked_cols):
            if abs(row - test_row) == abs(col - test_col):
                return True
        return False

    def to_board(self, picked_cols):
        return ["."*col + "Q" + "."*(self.N-1-col) for col in picked_cols]

# TODO: draw_answers
        
def main():
    NQueen(2)
    
if __name__ == '__main__':
    main()
