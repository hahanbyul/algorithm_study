# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:16:14 2017

@author: hanbyulkim
"""
import numpy as np
cache = []

def main():
    #seq = '3 3 3 1 2 3 2 2 2 1'
    seq = '1 744 755 4 897 902 890 6 777'
    seq_array = np.sort(np.array([int(x) for x in seq.split()]))

    s = 3
    
    global cache
    cache = [[-1 for _ in range(len(seq_array))] for _ in range(s)]    
    
    print("min sum: %d" % quant(seq_array, 0, s))


def quant(seq, begin_index, s):
    if cache[s-1][begin_index] != -1: return cache[s-1][begin_index]    

    if s == 1:
        if cache[0][begin_index] != -1: return cache[0][begin_index]
        #print("last seq: %s" % seq)
        #print("begin: %d" % begin_index)
        cache[0][begin_index] = min_square_error_sum(seq)
        return cache[0][begin_index]
    
    ret = np.inf
    for i in range(1, len(seq) - (s-1) + 1):
        #print("seq: %s" % seq)
        #print("s: %d" % s)
        ret = min(ret, min_square_error_sum(seq[:i]) + quant(seq[i:], begin_index + i, s-1))
    
    cache[s-1][begin_index] = ret
    return ret
    
def min_square_error_sum(seq):
    return np.sum((seq - np.round(np.mean(seq))) ** 2)
    
if __name__ == '__main__':
    main()