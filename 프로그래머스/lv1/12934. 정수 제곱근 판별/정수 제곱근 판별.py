def solution(n):
    answer = ((n**(1/2))+1)*((n**(1/2))+1) if int(n**(1/2)) == n ** (1/2) else -1 
    return answer