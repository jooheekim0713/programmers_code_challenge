import math

def solution(a, b):
    if a%2==0 and b%2==0:
        answer = abs(a-b)
    elif a%2 ==1 and b%2 == 1:
        answer = math.pow(a,2)+math.pow(b,2)        
    elif a%2 ==0 or b%2==0:
        answer = 2*(a+b)
    return answer