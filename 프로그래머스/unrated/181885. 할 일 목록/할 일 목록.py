def solution(todo_list, finished):
    return [ i[0] for i in zip(todo_list,finished) if i[1] == False]