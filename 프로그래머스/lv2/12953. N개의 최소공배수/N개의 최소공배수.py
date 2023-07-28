from math import gcd

def lcm(a,b):
    return (a*b)//gcd(a,b)

def solution(arr):
    answer = lcm(arr[0],arr[1])
    for b in arr[2:]:
        answer = lcm(answer,b)
    return answer