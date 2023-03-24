function solution(n, m, section) {
    let answer = 0;
    const arr = Array.from({length:n},()=> 0);
    
    section.forEach(item => arr[item-1] = 1);
    let i = 0;
    
    while(i < arr.length) {
        if(arr[i] === 1) {
            answer++;
 			i += m;
        }
        else i++; 
    }
    return answer;
}