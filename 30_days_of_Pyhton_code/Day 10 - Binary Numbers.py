# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
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
    bi = bin(n)
    bins = str(bi)[2::]
    count=0
    maxi=0
    for i in bins:
        if i==str(1):
            count+=1
        else:
            maxi = max(maxi,count)
            count=0
    print(max(maxi,count))
