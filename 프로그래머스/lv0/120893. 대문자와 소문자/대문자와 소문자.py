def solution(my_string):
    answer = ''
    str = list(my_string)
    for x in str:
        if x.upper() != x:
            answer += x.upper()
        else:
            answer += x.lower()
    return answer