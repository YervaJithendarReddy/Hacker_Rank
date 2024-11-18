# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-arrays/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in arr[::-1]:
        print(i,end=" ")