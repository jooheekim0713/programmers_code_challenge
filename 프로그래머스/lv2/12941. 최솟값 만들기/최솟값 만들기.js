function solution(A,B){
    var answer = 0;
    //배열에서 하나씩 제거하기
    // A배열에서 가장 작은 수 * b배열에서 가장 큰 수 두 수를  pop()
    A.sort((a,b) => a-b);
    B.sort((a,b) => a-b);
    
    let len = A.length;
    while(len){
        answer += A[0] * B[len-1]
        A.shift();
        B.pop();
        len--;
    }
    
    return answer;
}