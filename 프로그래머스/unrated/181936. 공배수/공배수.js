function solution(number, n, m) {
    let answer = +(number % n === 0) && +(number % m === 0)
    return answer;
}