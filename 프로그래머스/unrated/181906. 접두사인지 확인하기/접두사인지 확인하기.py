def solution(my_string, is_prefix):
    return int(is_prefix in [my_string[:i] for i in range(1,len(my_string)+1)])