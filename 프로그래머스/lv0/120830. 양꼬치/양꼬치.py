def solution(n, k):
    stick = 12000
    drink = 2000
    free = int(n/10)

    answer = n*stick + (k -free)*drink
    return answer