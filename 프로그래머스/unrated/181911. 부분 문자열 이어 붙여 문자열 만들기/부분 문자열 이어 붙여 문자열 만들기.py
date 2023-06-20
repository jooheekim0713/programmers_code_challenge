def solution(my_strings, parts):
    idx = 0
    answer = ''
    for [x,y] in parts:
        answer += my_strings[idx][x:y+1]
        idx +=1
    return answer