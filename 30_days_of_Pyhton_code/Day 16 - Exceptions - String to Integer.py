# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

S = input()

try:
    print(int(S))
except ValueError:
    print("Bad String")
