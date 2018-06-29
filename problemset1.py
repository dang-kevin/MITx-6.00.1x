# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:42:53 2018

@author: kd_ch
""" 

s = 'azcbobobegghakl'
vowels = 0
for ch in s:
    if ch in 'aeiou':
        vowels += 1
print('Number of vowels: ' + str(vowels))

s = 'azcbobobegghakl'
count = 0
for i in range(len(s)-1):
    if s[i:i+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))

s = 'azcbobobegghakl'
temp = s[0]
longest = s[0]
for ch in s[1:]:
    if ch >= temp[-1]:
        temp += ch
        if len(temp) > len(longest):
            longest = temp
    else:
        temp = ch
print("Longest substring in alphabetical order is: " + str(longest))
