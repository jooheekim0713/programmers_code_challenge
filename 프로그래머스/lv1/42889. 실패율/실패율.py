def solution(N, stages):
    answer = {}
    denominator = len(stages)
    for stage in range(1,N+1):
        if denominator != 0:
            count = stages.count(stage)
            answer[stage] = count/denominator
            denominator -= count
        else:
            answer[stage] = 0
    return sorted(answer,key=lambda x: answer[x],reverse= True)