def solution(my_string, overwrite_string, s):
    length = len(overwrite_string)
    answer = my_string[0:s]+overwrite_string+my_string[s+length:len(my_string)]
    return answer