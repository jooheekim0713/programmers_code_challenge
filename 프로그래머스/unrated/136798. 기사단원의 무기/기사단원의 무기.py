def getDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    return len(divisorsList)

def solution(number, limit, power):
    return sum([getDivisor(i) if getDivisor(i) <= limit else power for i in range(number+1)])