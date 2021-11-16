import sys

string = list(sys.stdin.readline().strip())
string2 = []
n = int(sys.stdin.readline())

cursor = len(string)

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L":
        if len(string)==0:
            continue
        string2.append(string.pop())

    elif command[0] == "D":
        if len(string2)==0:
            continue
        string.append(string2.pop())

    elif command[0] == "B":
        if len(string)==0:
            continue
        string.pop()
    
    elif command[0] == "P":
        string.append(command[1])

string.extend(string2[::-1])
for i in range(len(string)):
    print(string[i],end="")

