# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/string-validators/problem
# Difficulty: Easy
# Max Score: 10
# ========================
#         Solution
# ========================

if __name__ == '__main__':
    s = input()

    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))


#  OR

if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    for i in s:
        if i.isalpha():
            print(True)
            break
    else:
        print(False)
    for i in s:
        if i.isdigit():
            print(True)
            break
    else:
        print(False)
    for i in s:
        if i.islower():
            print(True)
            break
    else:
        print(False)
    for i in s:
        if i.isupper():
            print(True)
            break
    else:
        print(False)