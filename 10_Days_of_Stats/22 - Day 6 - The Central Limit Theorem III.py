# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

s = 100
m = 500
sd = 80
z= 1.96
rng = 0.95

print(round(-1.96 * (sd/math.sqrt(s)) + m, 2))
print(round(1.96 * (sd/math.sqrt(s)) + m, 2))
