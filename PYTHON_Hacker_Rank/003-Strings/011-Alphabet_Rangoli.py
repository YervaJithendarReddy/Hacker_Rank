# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Difficulty: Easy
# Max Score: 20
# ========================
#         Solution
# ========================

n=input().split()
n=int(n[0])
a=".|."
for i in range(1,n):
    if i%2!=0: 
        d=i*a
        c=d.center(n*3,"-")
        d=""
        print(c)
print("WELCOME".center(n*3,"-"))
for i in range(n-1,0,-1):
    if i%2!=0:
        d=i*a
        c=d.center(n*3,"-")
        d=""
        print(c)