# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

N = int(input())
ARRAY = map(int, input().split())
l1 = list(ARRAY)

l1.sort()
HIGHEST_NUMBER = max(l1)

for i in range(len(l1)-1, -1, -1):
    if l1[i] < HIGHEST_NUMBER:
        break

print(l1[i])