def getDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
                
    return len(divisorsList)

def solution(number, limit, power):
    answer = 0
    list_a = [x+1 for x in range(number)]
    for a in list_a:
        div_res = getDivisor(a)
        answer += power if limit < div_res else div_res
            
    return answer