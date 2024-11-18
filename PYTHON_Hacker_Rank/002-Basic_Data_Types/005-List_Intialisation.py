# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================


N = int(input())
lst=[]
lst1=[]
for i in range(N):
    a=input().split()
    lst.append(a)
for i in lst:
    if i[0]=='insert':
        lst1.insert(int(i[1]),i[2])
    elif i[0]=='print':
        print(lst1)
    elif i[0]=='remove':
        lst1.remove(i[1])
    elif i[0]=='append':
        lst1.append(i[1])
    elif i[0]=='sort':
        lst1.sort()
    elif i[0]=='pop':
        lst1.pop()
    elif i[0]=='reverse':
        lst1.reverse()