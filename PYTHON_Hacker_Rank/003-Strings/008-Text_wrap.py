# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/text-wrap/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#  or

import textwrap

def wrap(string, max_width):
    l1=[]
    a=""
    for i in range(len(string)):
        if (i%max_width==0) & (i!=0):
            a="".join(l1)
            print(a)
            l1=[]
            l1.append(string[i])
        else:
            l1.append(string[i])
    a="".join(l1)
    return a
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)