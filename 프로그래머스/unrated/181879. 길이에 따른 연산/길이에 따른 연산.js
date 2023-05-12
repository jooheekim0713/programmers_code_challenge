function solution(num_list) {
    let answer = 0;
    
    if(num_list.length >= 11){
        for(const x of num_list){
            answer += x
        }
        
    }else if (num_list.length <= 10){
        answer = num_list.reduce((a,b) => a*b)
     }
    
    return answer;
}