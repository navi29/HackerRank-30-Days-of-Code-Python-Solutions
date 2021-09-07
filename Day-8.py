#---------------------------------------------
#Problem Statement:  https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}

for i in range(n):
    name = input()
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')