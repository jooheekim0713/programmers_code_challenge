from collections import Counter

def solution(k, tangerine):
    tan_dict = Counter(tangerine)
    
    tangerine.sort(key=lambda t: (-tan_dict[t],t))
    
    return len(set(tangerine[:k]))