# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty: Easy
# Max Score: 10

# ========================
#         Solution
# ========================

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)