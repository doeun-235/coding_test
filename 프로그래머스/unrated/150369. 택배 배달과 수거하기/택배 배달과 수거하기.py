def make_cur(arr,cap,n):
    cur, i  = [], n-1
    bag = cap
    while i >= 0 :
        if arr[i] > 0 :
            if bag == cap :
                quo, res = divmod(arr[i],cap)
                if res == 0 : cur.extend([i]*quo)
                else : cur.extend([i]*(quo+1))
                bag -= res
            else :
                if arr[i] < bag : bag -= arr[i]
                else :
                    arr[i] -= bag
                    bag = cap
                    continue
        i-=1
    return cur 

    
def solution(cap, n, deliveries, pickups):
    answer = 0       
    deli_cur = make_cur(deliveries,cap,n)
    pick_cur = make_cur(pickups,cap,n)
    
    if len(deli_cur) > len(pick_cur):
        pick_cur.extend([-1]*(len(deli_cur)-len(pick_cur)))
    elif len(deli_cur) < len(pick_cur):
        deli_cur.extend([-1]*(len(pick_cur)-len(deli_cur)))
            
    for i in range(len(deli_cur)):
        answer += 2*(max(deli_cur[i],pick_cur[i])+1)
    
    return answer    