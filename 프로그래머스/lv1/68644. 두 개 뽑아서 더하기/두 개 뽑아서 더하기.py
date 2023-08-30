def solution(numbers):
    answer = []
    for idx_1,x in enumerate(numbers):
        for idx_2,y in enumerate(numbers):
            if idx_1 != idx_2:
                answer.append(x+y)
            
    return sorted(list(set(answer)))