function solution(number) {
    let numArr = number.split('').map(v => Number(v));
    var answer = numArr.reduce((acc,curr) => acc+curr,0) % 9;
    return answer;
}