def divide_cluster(n,lost):
    ret = []
    frnt_cur, end_cur, cnt = lost[0], lost[0], 0
    for ind in lost:
        if ind - end_cur > 2 :
            ret.append((frnt_cur,end_cur, cnt))
            frnt_cur, end_cur = ind, ind
        else : end_cur, cnt = ind, cnt+1
    ret.append((frnt_cur,end_cur, cnt))
    return ret

def cnt_surplus(frnt,end,reserve):
    ret = list(filter(lambda x: (frnt-1<=x) and (x<=end+1),reserve))
    return len(ret)

def filter_common(x,y):
    x_set, y_set = set(x), set(y)
    x_diff = list(x_set.difference(y_set))
    y_diff = list(y_set.difference(x_set))
    return sorted(x_diff), sorted(y_diff)
    

def solution(n,lost,reserve):
    ans = 0
    lost, reserve = filter_common(lost,reserve) 
    cluster = divide_cluster(n,lost)
    for frnt,end,cnt in cluster:
        surplus = cnt_surplus(frnt,end,reserve)
        ans += min(cnt,surplus)
    return n-len(lost)+ans