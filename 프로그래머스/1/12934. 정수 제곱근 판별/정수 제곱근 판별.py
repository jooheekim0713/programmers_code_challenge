def solution(n):
    sqrt = n**(1/2)
    answer = (sqrt+1)*(sqrt+1) if int(sqrt) == sqrt else -1 
    return answer