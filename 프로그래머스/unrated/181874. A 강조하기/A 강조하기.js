function solution(myString) {
    var answer = [...myString.toLowerCase()].map(v=> v === 'a'?v.toUpperCase():v).join('');
    return answer;
}