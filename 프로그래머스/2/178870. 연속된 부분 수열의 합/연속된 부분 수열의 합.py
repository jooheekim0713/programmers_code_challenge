def solution(sequence, k):
    answers = []
    sum_1 = 0
    l = 0
    r = -1
    
    while True:
        if sum_1 < k:
            r += 1
            if r >= len(sequence):
                break
            sum_1 += sequence[r]
        else:
            sum_1 -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum_1 == k:
            answers.append([l, r])
    
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]