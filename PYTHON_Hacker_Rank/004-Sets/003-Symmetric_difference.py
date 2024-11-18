# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

m = int(input())

a = set(map(int, input().split()))

n = int(input())

b = set(map(int, input().split()))
c = a.difference(b)
d = b.difference(a)
e = c.union(d)
RESULT = list(e)

RESULT.sort()

for i in range(len(RESULT)):
    print(RESULT[i])