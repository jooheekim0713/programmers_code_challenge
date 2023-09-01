def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        answer += 1 if int(t[i:i+len(p)]) <= int(p) else 0
    return answer