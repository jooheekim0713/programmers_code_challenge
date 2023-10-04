import string

def solution(n, k):
    number = string.digits + string.ascii_uppercase
    q,r = divmod(n,k)
    return solution(q,k) + number[r] if q else number[r]