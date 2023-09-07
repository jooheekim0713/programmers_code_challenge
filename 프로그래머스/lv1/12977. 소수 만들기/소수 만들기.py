def solution(nums):
    answer = 0
    l = len(nums)
    
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                number = nums[i] + nums[j] + nums[k]
                if len([m for m in range(2, number) if number % m == 0]) == 0:
                    answer += 1

    return answer