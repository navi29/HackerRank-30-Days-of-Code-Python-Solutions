#---------------------------------------------
#Problem Statement:  https://www.hackerrank.com/challenges/30-data-types/problem
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

if __name__ == '__main__':
    N = int(input().strip())

    for i in range(10):
        print(str(N),"x 1 =",str(N*(i+1)))