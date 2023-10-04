def conv(n,k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

def isPrime(n):
    if n <=1 : return False
    i = 2
    while i*i <= n:
        if n %i == 0 : return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    answer = 0
    
    for num in s.split('0'):
        if not num : continue
        if isPrime(int(num)):
            answer +=1    
    return answer