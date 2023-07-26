from math import sqrt

def prime_list(n):
    answer = []
    for m in range(2,int(sqrt(n))+2):
        for p in answer:
            if m%p == 0 : break
        else : answer.append(m)
    return answer

def factorize(n,primes):
    ret = dict()
    for p in primes :
        k, temp = 0, n
        while True :
            if temp % p == 0:
                temp /= p
                k += 1
            else :
                ret[p] = k
                break
    return ret

def factor2divisor(factor_dict,n):
    ret = set()
    factor_list = sorted(list(factor_dict.keys()))
    arr = [0 for i in range(len(factor_list))]
    max_arr = [factor_dict[p] for p in factor_list]
    while True:
        arr[0] += 1
        for i in range(len(arr)-1):
            if arr[i] > max_arr[i]:
                arr[i], arr[i+1] = 0, arr[i+1]+1
        if arr[-1] > max_arr[-1] : break
        div = 1
        for i,p in enumerate(factor_list):
            div *= p ** arr[i]
        ret.add(div)
        ret.add(n//div)
    return sorted(ret)

def val(n,primes,primes_set):
    if n == 1 : return 0
    if n in primes_set : return 1
    arr, flag = [], 0
    for prime in primes :
        if n % prime == 0 :
            arr.append(prime)
            if n//prime <= 10000000 and flag == 0:
                return n//prime
            else : flag = 1
    else:
        if len(arr) == 0 : return 1
        else :
            factor_dict = factorize(n,arr)
            divisors = factor2divisor(factor_dict,n)
            divisors = list(filter(lambda x : x <= 10000000,divisors))
            return divisors[-1]

def solution(begin, end):
    answer = []
    primes = prime_list(end)
    primes_set = set(primes)
    for i in range(begin,end+1):
        answer.append(val(i,primes,primes_set))
    return answer