# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,aurthor,price):
        self.price = price
        super().__init__(title,aurthor)
    
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
