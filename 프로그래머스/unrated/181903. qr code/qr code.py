def solution(q, r, code):
    answer = ''
    for idx,x in enumerate(code):
        if (idx -r) % q == 0:
            answer += x
    return answer