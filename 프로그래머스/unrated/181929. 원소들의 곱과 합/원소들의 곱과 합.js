function solution(num_list) {
    let sum = Math.pow(num_list.reduce((acc, curr) => acc + curr,0),2)
    let mul = num_list.reduce((acc, curr) => acc * curr,1)
   
    return +(sum > mul);
}