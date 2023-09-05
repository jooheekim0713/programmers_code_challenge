def solution(name, yearning, photo):
    answer = []
    yearning_dict = dict(zip(name,yearning))

    for p in photo:
        score=0
        for name in p:
            if name in yearning_dict:
                score += yearning_dict[name]
        answer.append(score)
    return answer