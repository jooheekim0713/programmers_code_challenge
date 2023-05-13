function solution(todo_list, finished) {
    var answer = [];
    answer = todo_list.filter((v,i)=> !finished[i] && v)
    return answer;
}