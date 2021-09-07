#---------------------------------------------
#Problem Statement:  https://www.hackerrank.com/challenges/30-review-loop/problem
#---------------------------------------------
#Language: Python
#---------------------------------------------
#Solution:
#---------------------------------------------

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        string = input()
        odd = ""
        even = ""
        for j in range(0,len(string),2):
            odd = "".join((odd,string[j]))
            even = "".join((even,string[j+1]))

        print(odd, even)