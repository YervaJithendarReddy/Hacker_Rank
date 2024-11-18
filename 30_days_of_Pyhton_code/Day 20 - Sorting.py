# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-sorting/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                count+=1
            else:
                pass
                
    print("Array is sorted in {} swaps.".format(count))
    print('First Element:',a[0])
    print('Last Element:',a[-1])
    
