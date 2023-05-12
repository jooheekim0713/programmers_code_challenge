function solution(myString, pat) {
    let my_string = myString.toLowerCase();
    let pat_1 = pat.toLowerCase();
    
    return +my_string.includes(pat_1);
}