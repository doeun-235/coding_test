def change(my_,que):
    ret = my_.copy()
    for i in range(que[0],que[1]+1):
        ret[i] = my_[que[1]+que[0]-i]
    return ret

def solution(my_string, queries):
    ans = list(my_string)
    for que in queries :
        ans = change(ans,que)
    return ''.join(ans) 