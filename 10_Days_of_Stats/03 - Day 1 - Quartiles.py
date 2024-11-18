# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def median(n,arr):
    if n%2==0:
        ind1 = n//2
        ind2 = ind1-1
        return (arr[ind1]+arr[ind2])//2
    else:
        return arr[n//2]

def quartiles(arr):
    # Write your code here
    q1=median(n//2,arr[0:n//2])
    q2=median(n,arr)
    q3=median(n//2,arr[(n+1)//2::])
    return q1,q2,q3
c= quartiles(b)
print(c)
print(MEDIAN_U)
