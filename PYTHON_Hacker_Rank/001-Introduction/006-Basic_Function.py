# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/write-a-function/problem
# Difficulty: Medium
# Max Score: 10

# ========================
#         Solution
# ========================

def is_leap(YEAR):
    return YEAR % 4 == 0 and (YEAR % 400 == 0 or YEAR % 100 != 0)
YEAR = int(input())
print(is_leap(YEAR))