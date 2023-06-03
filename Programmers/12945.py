def solution(n):
    fl = 0; fr = 1;
    for i in range(n-1):
        temp = fr
        fr += fl
        fl = temp
    return fr % 1234567