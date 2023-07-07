def solution(arr, idx):
    arr1 = arr[idx:]
    if 1 in arr1:
        return arr1.index(1) + idx
    else:
        return -1