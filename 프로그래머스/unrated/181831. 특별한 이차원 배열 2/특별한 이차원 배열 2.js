function solution(arr) {
    var answer = 1;
    for(let i = 0; i< arr.length; i++){
        for(let j =0; j < arr.length; j++){
            if(arr[i][j] != arr[j][i]){
                answer = 0;
                return 0;
            }else{
                answer = 1;
            } 
        }
    }
    return answer;
}