# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N.symmetric_difference(SET_B)))