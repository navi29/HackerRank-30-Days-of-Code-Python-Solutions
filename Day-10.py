#---------------------------------------------
#Problem Statement:  https://www.hackerrank.com/challenges/30-binary-numbers/problem
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

n = int(input())

binary = bin(n)

length = []
for i in range(2,len(binary)):
    if binary[i]==str(1):
        j = i+1
        count = 1
        while j<len(binary):
            if binary[j]==str(0):
                break
            count += 1
            j += 1
        length.append(count)
if length:  print(max(length))
else: print(0)