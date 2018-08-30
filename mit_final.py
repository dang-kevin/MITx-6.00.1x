# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:27:21 2018

@author: kd_ch
"""

def isPalindrome(aString):
    '''
    aString: a string
    '''
    rev = ''
    for ch in aString:
        rev = ch + rev
    return aString == rev


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    odd_times = {}
    for num in L:
        if L.count(num) % 2 != 0:
            odd_times[num] = L.count(num)
    if len(odd_times) > 0:
        return max(odd_times)
        
    
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    value_count = {} #stores the # of times each value occurs in aDict
    keys = []
    for value in aDict.values():
        if value in value_count.keys(): 
            value_count[value] += 1
        else: 
            value_count[value] = 1
    for key in aDict.keys():
        if value_count[aDict[key]] == 1: 
            keys.append(key)
    return sorted(keys)


        