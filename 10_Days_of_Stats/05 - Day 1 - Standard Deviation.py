# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-standard-deviation
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

arr=[10, 40, 30, 50, 20]
d = []
mean = sum(arr)/len(arr)
for i in arr:
    dis = (i-mean)**2
    d.append(dis)
sum_of_d = sum(d)
sqr = math.sqrt(sum_of_d/len(arr))
sqr = round(sqr,1)
print(sqr)
