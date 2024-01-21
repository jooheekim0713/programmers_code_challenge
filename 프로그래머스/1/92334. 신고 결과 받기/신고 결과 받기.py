def solution(id_list, report, k):
    answer = []
    #하나하나씩 고고
    idObj ={id:0 for id in id_list}
    report = set(report)
    for i in report:
        idObj[i.split(' ')[1]] += 1
    
    #value가 k이상인 key를 찾자
    keyObj = [key for (key,value) in idObj.items() if value>=k]
    
    answerObj ={id:0 for id in id_list}
    for i in report:
        if i.split(' ')[1] in keyObj:
            answerObj[i.split(' ')[0]] += 1
    answer = [ value for (key,value) in answerObj.items()]
    return answer