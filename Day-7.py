#---------------------------------------------
#Problem Statement:  https://www.hackerrank.com/challenges/30-arrays/problem
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

if __name__ == "__main__":
    N = int(input())

    array = list(map(int,input().split()))
    newarray = array[::-1]

    for j in newarray:
        print(j,end=" ")