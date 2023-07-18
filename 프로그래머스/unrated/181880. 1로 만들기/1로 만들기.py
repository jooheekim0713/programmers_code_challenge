def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        num = num_list[i]
        while num > 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = (num -1) / 2
            answer += 1
            
    return answer