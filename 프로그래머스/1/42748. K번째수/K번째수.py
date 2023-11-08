def solution(array, commands):
    answer = []
    for comm in commands:
        list_a = sorted(array[comm[0]-1:comm[1]])
        answer.append(list_a[comm[2]-1])
    return answer