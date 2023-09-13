def solution(s):
    temp = ["",s[0]]
    
    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    return 1 if len(temp)==1 else 0