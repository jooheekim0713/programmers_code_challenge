def countOne(n):
    return bin(n).count('1')

def solution(n):
    i = 1
    while countOne(n) != countOne(n+i):
        i += 1
    return n + i


