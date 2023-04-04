function solution(name, yearning, photo) {
    let obj = new Map();
    
    for(let i =0; i< name.length; i++){
        obj.set(name[i],yearning[i])
    }
        return photo.map((v) => v.map(i => 
                                   obj.has(i)?obj.get(i):0).reduce((acc, curr) => acc+curr));
}