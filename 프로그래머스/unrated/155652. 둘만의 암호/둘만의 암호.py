def cha_wheel(skip):
    wheel = [chr(i) for i in range(97,123)]
    return list(filter(lambda x : x not in skip,wheel))

def roll_wheel(cha,wheel,l):
    return wheel[(wheel.index(cha) + l) % len(wheel)]

def solution(s, skip, index):
    wheel = cha_wheel(skip)
    answer = list(map(lambda x : roll_wheel(x,wheel,index),list(s))) 
    return ''.join(answer)