import sys
from sys import stdin
            
n = int(sys.stdin.readline())
li_1=list(map(int,input().split()))
li_1.sort()
m=int(input())
li_2=list(map(int,input().split()))

dic = dict()

for i in li_1:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in li_2:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")
