# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def weightedMean(X, W):
    # Write your code here
    s1 = []
    for i in range(len(X)):
        s1.append(X[i]*W[i])
    val = round(sum(s1)/sum(W),1)
    print(val)
