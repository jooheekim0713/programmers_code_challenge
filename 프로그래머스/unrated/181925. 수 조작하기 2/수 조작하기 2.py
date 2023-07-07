def solution(numLog):
    answer = ''
    for idx,v in enumerate(numLog):
        if idx > 0:
            num = numLog[idx]-numLog[idx-1]
            if num == 1:
                answer += 'w'
            elif num == -1:
                answer += 's'
            elif num == 10:
                answer += 'd'
            elif num == -10:
                answer += 'a'
    return answer