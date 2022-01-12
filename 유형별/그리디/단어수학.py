import sys

n = int(sys.stdin.readline())
string = []

# 단어 입력받기
for _ in range(n):
    string.append(input())

# 길이 만큼 정렬
string_sorted = sorted(string,key=lambda x:len(x),reverse=True)

# 길이 체크 -> 맞게 출력됨 
for i in string_sorted:
    print(i)
