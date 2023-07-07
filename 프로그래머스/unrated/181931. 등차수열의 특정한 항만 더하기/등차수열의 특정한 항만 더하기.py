def solution(a, d, included):
    arr = [a+(i*d) for i in range(len(included))]
    answer = 0
    for idx,v in enumerate(included):
        if v:
            answer += arr[idx]
    return answer