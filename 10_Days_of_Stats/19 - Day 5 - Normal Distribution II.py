# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

mean, std = list(map(float, input().rstrip().split()))
X_1 = float(input())
X_2 = float(input())

def normal_distribution(X, mean, std):
    '''Function to calculate the normal distribution'''
    return 1/2*(1+math.erf((X-mean)/(std*math.sqrt(2))))

# grade >80
print(round((1-normal_distribution(X_1, MU, SD))*100, 2))

# grade >= 60
print(round((1-normal_distribution(X_2, MU, SD))*100, 2))

# grade <60
print(round((normal_distribution(X_2, MU, SD))*100, 2))
