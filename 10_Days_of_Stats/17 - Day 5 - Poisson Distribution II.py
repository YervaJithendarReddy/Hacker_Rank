# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

x, y = [float(num) for num in input().split(" ")]
xcost = 160 + 40*(x +x**2)
ycost = 128 + 40*(y+ y**2)

print(round(xcost, 3))
print(round(ycost, 3))
