#---------------------------------------------
#Problem Statement:  [statement](https://www.hackerrank.com/challenges/30-class-vs-instance/problem)
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

class Person:

    def __init__(self, intialAge):
        if intialAge > 0:
            self.age = intialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")

t = int(input())
for i in range(t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(3):
        p.yearPasses()
    p.amIOld()
    print("")