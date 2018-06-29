# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:04:57 2018

@author: Kevin
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    
    >>> closest_power(3,12)
    2
    '''
    exponent = 1
    while base ** exponent < num:
        exponent += 1
    if base ** exponent - num < num - base ** (exponent - 1):
        return exponent
    else:
        return exponent - 1
    
    
def getSublists(L, n):
    '''
    L: non-empty list
    0 < n <= len(L)
    This function returns a list of all possible sublists in L of length n 
    without skipping elements in L. The sublists in the returned list should 
    be ordered in the way they appear in L, with those sublists starting from 
    a smaller index being at the front of the list.
    
    >>> L = [1, 1, 1, 1, 4]
    >>> n = 2
    >>> getSublists(L, n)
    [[1, 1], [1, 1], [1, 1], [1, 4]]
    '''
    lst = []
    for i in range(len(L)-n+1):
        lst.append(L[i:i+n])
    return lst


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    Returns a list of keys which have been assigned a value of target.
    
    >>> aDict = {'a': 1, 'b': 2}
    >>> target = 1
    >>> keysWithValue(aDict, target)
    ['a']
    '''
    keys = []
    for k in aDict:
        if aDict[k] == target:
            keys.append(k)
    return keys


def sumDigits(N):
    '''
    N: a non-negative integer
    Returns the sum of the digits in an integer, using recursion
    
    >>> sumDigits(123)
    6
    '''
    if N < 10:
        return N
    else:
        return sumDigits(N // 10) + N % 10  # N % 10 gives rightmost digit
    
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    
    >>> L = [0, -10, 5, 6, -4]
    >>> print(applyF_filterG(L, f, g))
    6
    >>> print(L)
    [5, 6]
    """
    clone = L[:]
    for i in clone:
        if g(f(i)) != True:
            L.remove(i)
    if len(L) > 0:
        return max(L)
    else:
        return -1

# Example functions for function applyF_filterG
def f(i):
    return i + 2

def g(i):
    return i > 5


if __name__ == '__main__':
    import doctest
    doctest.testmod()
