# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:35:49 2017

@author: hanbyulkim
"""
cache = dict()
min_good_seq = []

def is_good(seq, begin_index):
    #print(seq)
    if len(seq) == 2:
#        if seq[0] == seq[1]: # if bad
        return seq[0] != seq[1]

    for end_index in range(1, int(len(seq))+1):
        return is_good(seq[1:], begin_index + 1) and seq[:end_index] != seq[end_index:2*end_index]

def all_123_seq(picked, N):
    global min_good_seq
    if N == 0:
        good = is_good(picked, 0)
        if good:
            print("%s => %r" % (picked, is_good(picked, 0)))
            for pick in picked:
                min_good_seq.append(pick)
            return True
            
        return False
        
    for i in range(1, 3+1):
        picked.append(i)
        good = all_123_seq(picked, N-1)
        if good:
            return True
        picked.pop()
    
def main():
    N = 4
    good = all_123_seq([], N)
    print(min_good_seq)
    #is_good("111111", 0)
    #print(min_good_seq(N))
    
        
if __name__ == '__main__':
    main()