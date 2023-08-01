def count_divisor(number):
    num_check = [1 for _ in range(number)]
    for n in range(2,number+1):
        for i in range(n-1,number,n): num_check[i] += 1
    return num_check 

def solution(number, limit, power):
    divisor_num = count_divisor(number)
    answer = list(map(lambda x : x if x <= limit else power,divisor_num))
    return sum(answer)