def solution(n):
    answer = 0
    #0~n까지 자연수 n으로 나누어서 나누어 떨어지는 약수
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer