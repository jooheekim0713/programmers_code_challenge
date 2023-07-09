def solution(myString):
    arr = myString.split('x')
    arr.sort()
    answer = []
    for i in arr:
        if i != "":
            answer.append(i)
    return answer