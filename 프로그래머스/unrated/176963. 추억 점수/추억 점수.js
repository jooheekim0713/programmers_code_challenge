function solution(name, yearning, photo) {
    var answer = [];
    let obj = new Map();
    for(let i =0; i< name.length; i++){
        obj.set(name[i],yearning[i])
    }
    answer =photo.map((v) => v.map(i => 
                                   obj.has(i)?obj.get(i):0).reduce((acc, curr) => acc+curr))
    return answer;
}