# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

from math import factorial, exp

mean = float(input())
k = int(input())

poisson = ((mean ** k) * exp(-mean)) / factorial(k)

print("%.3f" % poisson)

## Read from Tutorial To understand What is Possion distribution and the formula used above
### ==>> https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial

