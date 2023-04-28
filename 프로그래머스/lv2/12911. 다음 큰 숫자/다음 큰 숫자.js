function solution(n) {
    let binN = n.toString(2);
    let binOne = binN.split('').filter(i => i == 1).length
    let flag = 1;
    
    //찾을때까지 
    //찾으면 return 
    while(flag){
    ++n;
        if(binOne === n.toString(2).split('').filter(i => i == 1).length){
            return n;
        }       
    }
}