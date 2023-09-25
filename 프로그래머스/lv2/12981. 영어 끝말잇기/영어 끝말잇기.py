def solution(num, lst):
    elst = []
    cnt = 0
    for i in range(1, len(lst)):
        ans = i // num +1 
        ans2 = i % num + 1
        if lst[i] in lst[:i]:
            print("ch")
            return [ans2, ans]
        elif lst[i][0] != lst[i-1][-1]:
            print("ch", i)
            return [ans2, ans]
    else:
        return [0,0]