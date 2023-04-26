function solution(s){
    var answer = true;
    let stack = s.split('');
    let arr = [];
    if(stack[0] === ')') return false;
    for(let i = 0; i < stack.length; i++){
        if(stack[i] === '(') arr.push(stack[i]);
        else {
            arr.pop();
        }
        
    }
    
    answer = arr.length === 0
    return answer ;  
}