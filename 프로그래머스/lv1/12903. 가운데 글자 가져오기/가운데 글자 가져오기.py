def solution(s):
    answer = ''
    mid = len(s) // 2
    if len(s) % 2 == 1:
        answer += s[mid]
    else:
        answer += s[mid-1:mid+1]
    return answer