function solution(n, k) {
    var answer = [];
    let count = parseInt(n / k);
    for(let i = 1; i <= count; i++){
        answer.push(k*i)
    }
    return answer;
}