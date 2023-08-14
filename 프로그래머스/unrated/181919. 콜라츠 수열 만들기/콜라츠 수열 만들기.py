def collatz(n,arr):
    if n % 2 == 1 : new = 3*n +1
    else : new = n//2
    return (new,arr+[new])

def solution(n):
    arr = [n]
    while n > 1 :
        n, arr = collatz(n,arr)
    return arr