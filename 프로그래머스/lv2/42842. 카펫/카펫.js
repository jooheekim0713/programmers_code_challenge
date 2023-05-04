function solution(brown, yellow) {
    var answer = [];
    let sum = brown + yellow;
    
    for(let column = 3; column <= brown; column++){
        if(sum % column === 0){
            let row = sum / column;
            if((column-2) * (row-2) === yellow){
                return [row, column];
            }
        }
    }
    return answer;
}