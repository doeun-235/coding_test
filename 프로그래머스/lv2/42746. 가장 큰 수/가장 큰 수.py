from functools import cmp_to_key
from math import gcd

def cmp(a,b):
    LCM = len(a)*len(b) // gcd(len(a),len(b))
    A = a * (LCM//len(a))
    B = b * (LCM//len(b))
    for i in range(LCM):
        if A[i] > B[i]: return 1
        elif A[i] < B[i]: return -1
        else : continue
    else : return 0

def solution(numbers):
    numbers_list = list(map(str,numbers))
    temp = (sorted(numbers_list,key=cmp_to_key(cmp)))[::-1]
    return ''.join(temp) if temp[0] !='0' else '0'