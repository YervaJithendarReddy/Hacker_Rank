# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-interquartile-range
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2

# Create array
N = int(input())
VALUES = list(map(int, input().split()))
FREQUENCY = list(map(int, input().split()))

ARRAY = []

for i in range(N):
    ARRAY += [VALUES[i]] * FREQUENCY[i]
ARRAY = sorted(ARRAY)

# Find interquartile_range
INTERQUARTILE_RANGE = float(find_median(ARRAY[len(ARRAY) // 2 + len(ARRAY) % 2:]) - find_median(ARRAY[:len(ARRAY)//2]))

print(INTERQUARTILE_RANGE)


or 

a=[6, 12, 8, 10, 20, 16]
b=[5, 4, 3, 2, 1, 5]
c = []
for i in range(len(a)):
    for j in range(b[i]):
        c.append(a[i])
c.sort()
print(c)
n=len(c)
def qurtile(l1):
    n = len(l1)
    value=0
    if n%2==0:
        ind1 = n//2
        ind2 = ind1-1
        value = (l1[ind1]+l1[ind2])/2
    else:
        value = l1[n//2]
    return value
q1 = qurtile(c[0:n//2])
q3 = qurtile(c[n//2::])
print(q3-q1)