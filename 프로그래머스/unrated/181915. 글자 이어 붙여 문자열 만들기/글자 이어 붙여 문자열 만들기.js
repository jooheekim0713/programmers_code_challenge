function solution(my_string, index_list) {
    var answer = '';
    let strArr = [...my_string]

    for(let i = 0; i < index_list.length; i++){
        answer += strArr[index_list[i]]
    }
    return answer;
}