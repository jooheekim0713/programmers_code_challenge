def solution(x):
    total = sum(list(map(int,str(x))))
    return False if x % total != 0 else True