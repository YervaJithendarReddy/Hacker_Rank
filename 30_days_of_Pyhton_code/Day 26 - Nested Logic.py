# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-nested-logic/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

# Enter your code here. Read input from STDIN. Print output to STDOUT
date1 = list(map(int,input().split()))
date2 = list(map(int,input().split()))
d1 = date1[0]
m1 = date1[1]
y1 = date1[2]
d2 = date2[0]
m2 = date2[1]
y2 = date2[2]

fine = 0
if d2 == d1 and m2==m1 and y2==y1:
    fine = fine
elif d1>d2 and m1==m2 and y1==y2:
    ndays = d1-d2
    fine = 15*ndays
elif m1>m2 and y1==y2:
    nm = m1-m2
    fine = 500*nm
elif y1!=y2:
    fine = 10000
print(fine)
