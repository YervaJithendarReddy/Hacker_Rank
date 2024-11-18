# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks)
a=student_marks[query_name]
b=sum(a)/len(a)
print("{:.2f}".format(b))
