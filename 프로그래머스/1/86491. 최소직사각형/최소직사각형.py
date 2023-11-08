def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    answer = max([x[0] for x in sizes]) * max([x[1] for x in sizes])
    return answer