def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i,val in enumerate(completion):
        if participant[i] != completion[i]:
            return participant[i]
    
    return  participant[-1]