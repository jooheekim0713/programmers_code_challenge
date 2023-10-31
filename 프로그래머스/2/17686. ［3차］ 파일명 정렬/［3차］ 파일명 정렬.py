import re

def solution(files):
    lst = [re.split('([0-9]+)', file) for file in files]
    lst = sorted(lst, key = lambda x : (x[0].upper(), int(x[1])))
    return [''.join(i) for i in lst]