def solution(my_string):
    answer = [0 for _ in range(52)]
    for str in my_string:
        if str.isupper(): k = 65
        else: k = 71
        answer[ord(str)-k] += 1
    return answer