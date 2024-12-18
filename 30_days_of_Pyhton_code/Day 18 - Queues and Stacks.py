# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-queues-stacks/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================


import sys

class Solution:
    stack = []
    queue = []
    
    def pushCharacter(self,char):
        self.stack.append(char)
        
    def enqueueCharacter(self,char):
        self.queue.append(char)
        
    def popCharacter(self):
        value = self.stack[-1]
        self.stack.pop(-1)
        return value
        
    def dequeueCharacter(self):
        value = self.queue[0]
        self.queue.pop(0)
        return value
    # Write your code here

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    