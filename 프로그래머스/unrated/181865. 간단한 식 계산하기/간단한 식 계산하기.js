function solution(binomial) {
    let [a, op, b] = binomial.split(" ")
    var answer = 0;
    switch(op){
        case '+':
            answer = Number(a)+Number(b);
            break;
        case '-':
            answer = Number(a)-Number(b);
            break;
        case '*':
            answer = Number(a)*Number(b);
            break;
    }
    return answer;
}