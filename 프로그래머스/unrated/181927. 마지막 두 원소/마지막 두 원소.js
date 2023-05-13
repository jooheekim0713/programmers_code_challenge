function solution(num_list) {
    let answer = num_list.slice();
    if(num_list.at(-1) > num_list.at(-2)){
        answer.push(num_list.at(-1) - num_list.at(-2));
    }else{
        answer.push(num_list.at(-1)*2);
    }
    console.log(num_list.at(-1))
    return answer;
}