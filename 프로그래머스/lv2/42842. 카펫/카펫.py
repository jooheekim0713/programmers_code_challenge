def solution(brown, yellow):
    total = brown +yellow
    for column in range(3, int(total/3)+1):
        if total% column == 0:
            row = int(total/column)
            if row <= column and (column -2)*(row-2) == yellow:
                return [column, row]