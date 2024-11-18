# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

num = int(input())
dic = {}
for i in range(num):
    l1 = input().split()
    key = l1[0]
    value = l1[1]
    dic[key]=int(value)
    l1=[]
try:
    while True:
        x = input()
        if len(x)>0:
            if x in dic.keys():
                print(f'{x}={dic[x]}')
            else:
                print("Not found")
            x=''
        else:
            break
except:
    "ignore"