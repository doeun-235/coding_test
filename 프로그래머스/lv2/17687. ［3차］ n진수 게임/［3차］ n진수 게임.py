from math import log, ceil
from copy import deepcopy

def n_digit(n):
    digit = [str(i) for i in range(min(10,n))]
    if n > 10 : digit.extend(['A','B','C','D','E','F'][:n-10])
    return digit

def next_nary(n_rvs,n):
    n_rvs[0] += 1
    for i in range(len(n_rvs)-1):
        if n_rvs[i] == n :
            n_rvs[i] = 0
            n_rvs[i+1] += 1
        else : break
    else :
        if n_rvs[-1]==n :
            a = len(n_rvs)
            n_rvs = [0 for _ in range(a)]
            n_rvs.append(1)
    return n_rvs
     
def narynum(n,limit):
    digit = n_digit(n)
    cur_n_rvs=[0]
    ret = []
    for i in range(limit+1):
        add = [digit[i] for i in cur_n_rvs] 
        ret.extend(add[::-1])
        cur_n_rvs = next_nary(cur_n_rvs,n)
    return ret

def solution(n, t, m, p):
    answer = ''
    limit = ceil(log(p+(t-1)*m,n))
    total = narynum(n,n**limit)
    return ''.join(total[p-1:p+(t-1)*m:m])

