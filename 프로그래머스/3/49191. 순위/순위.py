def solution(n, results):
    answer = 0
    # n 길이에 맞는 board 세팅
    board = [[0]*n for _ in range(n)]
    #경기 결과를 board에 세팅
    #a가 b를 이기면 board[a-1][b-1]에 1 과 board[b-1][a-1] 에 -1을 세팅
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #자기 자신인 경우, 또는 이기거나 진경우 넘어간다. 
                if i == j or board[i][j] in [1,-1]:
                    continue
                #만약 i 선수가 k선수를, k선수가 j 선수를 이겼다면
                #i선수 는 언제나 j 선수를 이긴다.
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer