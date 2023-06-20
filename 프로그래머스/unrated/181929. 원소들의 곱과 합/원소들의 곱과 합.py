def solution(num_list):
    sum1 = sum(num_list)
    mul = 1
    for x in num_list:
        mul *= x
    if(sum1 **2 > mul):
        answer = 1
    else:
        answer = 0
    return answer