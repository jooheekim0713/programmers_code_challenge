function solution(num_list) {
    var answer = 0;
    let even = []
    let odd = []
    let evenString = "";
    let oddString = "";
    
    for(let x of num_list){
        if(x % 2 == 0) even.push(x)
        else odd.push(x)
    }
    
   for(let x of even){
       evenString += x;
   }
    
   for(let x of odd){
       oddString += x;
   }
    answer = Number(evenString) + Number(oddString);
    return answer;
}