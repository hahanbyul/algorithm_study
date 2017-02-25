# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:52:04 2017

@author: hanbyulkim
"""
import numpy as np

"""
def pi(str_length, num_list):
    for i in range(3,5+1):
        remain = str_length - i
        if remain < 0:
            return
        
        num_list.append(i)
        if remain == 0:
            print(num_list)
            return
        
        pi(str_length - i, num_list)
        num_list.pop()
        
def dfs(num_list, depth):
    if depth == 0: 
        print(num_list)        
        return
        
    for i in range(3, 5+1):
        num_list.append(i)
        dfs(num_list, depth - 1)
        num_list.pop()
        
def pi2(num_list, str_length):
    if str_length == 0: 
        print(num_list)   
        return
        
    for i in range(3, 5+1):
        if str_length - i < 0:
            return
            
        num_list.append(i)
        pi2(num_list, str_length - i)
        num_list.pop()
"""
cache = [ -1 for i in range(1000) ]

def pi(num_list, string, begin_index):
    if cache[begin_index] >= 0:
        return cache[begin_index]
    
    if len(string) == 0: 
        #print(num_list)
        #print(partial_sum)
        
        """
        if partial_sum < minimum:
            minimum = partial_sum
        print(minimum)
        """
        return 0
        
    elif len(string) < 3:
        return -1
        
    scores = np.zeros((3,1))
    for i in range(3):
        scores[i] = score(string[:i+2])
    
    for i in range(3, 5+1):
        if len(string) - i < 0:
            return -1
        
        num_list.append(i)
        result = pi(num_list, string[i:], begin_index + i)
        cache[begin_index] = result        
        
        if result >= 0:
            return result + scores[i-2]
        num_list.pop()

def pi2(string, begin_index):
    print(string)
    print(begin_index)
    
    if cache[begin_index] >= 0:
        return cache[begin_index]
        
    if len(string) >= 3 and len(string) <= 5: 
        cache[begin_index] = score(string)
        return cache[begin_index]
        
    elif len(string) < 3:
        return np.inf
    
    result = min(score(string[:3]) + pi2(string[3:], begin_index + 3), score(string[:4]) + pi2(string[4:], begin_index + 4), score(string[:5]) + pi2(string[5:], begin_index + 5))   
    cache[begin_index] = result
    return result
    
def score(pattern):
    arr = np.array([int(i) for i in pattern])
    diff = np.diff(arr)
    
    if all(diff == 0):
        return 1
    elif all(diff == 1) or all(diff == -1):
        return 2
    elif (len(pattern) == 3 and pattern[0] == pattern[2]) or len(principal_period(pattern)) == 2 or len(principal_period(pattern[1:])) == 2:
        return 4
    elif all(diff == diff[0]):
        return 5
    else:
        return 10
    
def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return [] if i == -1 else s[:i]