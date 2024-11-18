# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

x = int(input())
y = int(input())
z = int(input())
num = int(input())

result = []

for a in range(0, x + 1):
    for b in range(0, y + 1):
        for c in range(0, z + 1):
            if (a + b + c) != Num:
                result.append([a, b, c])

print(result)