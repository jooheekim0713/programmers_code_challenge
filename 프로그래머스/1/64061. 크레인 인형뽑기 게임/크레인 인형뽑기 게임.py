def solution(board, moves):
    answer = 0
    basket = [0]
    
    for move in moves:
        for i in range(len(board)):
            item = board[i][move-1]
            if item != 0:
                basket.append(item)
                if(basket[-1] == basket[-2]):
                    answer +=2
                    basket.pop()
                    basket.pop()
                board[i][move-1] = 0 
                break
    #선택된 상품을 바구니에 넣고 item을 0 으로 바꾼다.
    
    return answer