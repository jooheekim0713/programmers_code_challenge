def solution(num_list, n):
    num = 0
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[n*(num):n*(num+1)])
        num +=1
    return answer