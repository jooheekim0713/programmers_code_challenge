function solution(a, b) {
    var answer = Math.max(Number(String(a)+b) , 2* a* b);
    return answer;
}