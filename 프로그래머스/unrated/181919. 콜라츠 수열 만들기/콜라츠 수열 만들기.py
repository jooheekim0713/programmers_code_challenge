def solution(n):
    answer = [n]
    while(n >1):
        if n %2 == 0:
            n = int(n/2)
        else:
            n = 3* int(n) +1
        answer.append(n)
    return answer