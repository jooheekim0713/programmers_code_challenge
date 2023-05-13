function solution(before, after) {
    var answer = 1;
    let sH = new Map();
    for(let x of before){
        if(sH.has(x)) sH.set(x, sH.get(x)+1);
        else sH.set(x,1);
    }
    
    for(let x of after){
        if(!sH.has(x) || sH.get(x) === 0) return 0;
        sH.set(x,sH.get(x) -1);
    }
    return answer;
}