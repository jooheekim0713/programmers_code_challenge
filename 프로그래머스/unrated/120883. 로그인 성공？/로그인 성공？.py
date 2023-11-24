def solution(id_pw, db):
    answer = 'fail'
    for d in db:
        id,pw = d
        if id == id_pw[0] and pw == id_pw[1]:
            answer = 'login'
        elif id == id_pw[0] and pw !=id_pw[1]:
            answer = 'wrong pw'
            
    return answer