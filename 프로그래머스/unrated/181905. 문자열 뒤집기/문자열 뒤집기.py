def solution(my_string, s, e):
    answer = my_string[:s]
    reverse_str = ''
    for c in my_string[s:e+1]:
        reverse_str = c + reverse_str
    return answer+reverse_str+my_string[e+1:]