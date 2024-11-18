# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    students = []
    for n in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second = sorted(list(set([score for name, score in students])))[1]
    print('\n'.join([name for name, score in sorted(students) if score == second]))