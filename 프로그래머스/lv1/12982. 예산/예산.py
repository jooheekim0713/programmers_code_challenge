def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    
    if sum(d) <= budget:
        answer = len(d)
    else:
        for idx,val in enumerate(sorted_d):
            budget -= val
            if budget < 0: 
                answer =idx
                break
    return answer