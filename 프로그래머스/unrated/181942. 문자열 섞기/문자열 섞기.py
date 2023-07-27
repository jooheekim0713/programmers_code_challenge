def solution(str1, str2):
    answer = ''
    for idx,val in enumerate(str1):
        answer += val
        answer += str2[idx]
    return answer