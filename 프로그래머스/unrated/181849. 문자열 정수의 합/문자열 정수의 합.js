function solution(num_str) {
    var answer = num_str.split("").map(v=> Number(v)).reduce((acc,curr)=>acc+curr,0);
    return answer;
}