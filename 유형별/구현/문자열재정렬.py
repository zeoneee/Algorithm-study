from curses.ascii import isdigit

s = list(input())
result = 0
for i in range(len(s)):
    if isdigit(s[i]):
        result += int(s[i])
        s.pop(s[i])
s.sort()
s += str(result)
print(s)