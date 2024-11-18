# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-tuples/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

N = int(input())
print(hash(tuple(map(int, input().split()))))