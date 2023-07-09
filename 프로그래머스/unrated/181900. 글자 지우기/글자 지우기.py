def solution(my_string, indices):
    arr = list(my_string)
    indices.sort(reverse=True)
    for i in indices:
        arr.pop(i)
    return ''.join(arr)