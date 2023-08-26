def solution(price, money, count):
    answer = abs(min(money - sum([price*i for i in range(1,count+1)]),0))
    return answer