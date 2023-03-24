function solution(food) {
    var answer = '';
	for(let i = 0; i < food.length ; i++){
        if(Math.floor(food[i]/2) != 0){
        	answer += (i+"").repeat(food[i]/2)
        }        
    }
   
    reversedAns = [...answer].reverse().join('')+""
    return answer + 0 + reversedAns;
}