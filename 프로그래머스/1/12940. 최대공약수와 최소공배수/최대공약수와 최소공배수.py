import math

def solution(n, m):
    gcd = lambda a,b : math.gcd(a,b)
    lcm = lambda a,b : (a*b)/math.gcd(a,b)
    return [gcd(n, m), lcm(n, m)]