def solution(rsp):
    rspObj = {
        '2':'0',
        '0':'5',
        '5':'2'
    }
    return ''.join([rspObj[i] for i in rsp])