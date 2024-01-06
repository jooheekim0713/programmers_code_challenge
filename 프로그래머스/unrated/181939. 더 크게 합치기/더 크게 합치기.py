def solution(a, b):
    int_ab = int(str(a)+str(b))
    int_ba = int(str(b)+str(a))
    return max(int_ab, int_ba)