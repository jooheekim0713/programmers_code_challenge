import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    int_ = set(str1) & set(str2)
    uni = set(str1) | set(str2)

    if len(uni) == 0 :
        return 65536

    inter = sum([min(str1.count(i), str2.count(i)) for i in int_])
    union = sum([max(str1.count(u), str2.count(u)) for u in uni])

    return math.floor((inter/union)*65536)
