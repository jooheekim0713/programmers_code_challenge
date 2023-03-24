function solution(n) {
    var answer = Number.MAX_SAFE_INTEGER;
    for(let i =0; i < n; i++){
        if(n %i == 1){
            answer = i;
            break;
        }         
    }
    return answer;
}