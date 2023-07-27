def solution(before, after):
    answer = 0
    list_b = list(before)
    list_a = list(after)
    for i in list_b:
        if i in list_a:
            list_a.remove(i)
    return 1 if len(list_a) == 0 else 0