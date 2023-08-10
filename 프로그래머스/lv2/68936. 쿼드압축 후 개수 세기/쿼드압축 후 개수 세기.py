def quadfy(arr,cnt):
    ret = []
    for i in range(0,len(arr),2):
        line = []
        for j in range(0,len(arr),2):
            val = (sum([arr[i][j],arr[i][j+1],
                      arr[i+1][j],arr[i+1][j+1]]))
            check = ( 
                    (arr[i][j] == 0) + (arr[i][j+1] == 0)
                    + (arr[i+1][j] == 0) + (arr[i+1][j+1] == 0)
                )
            if 0 < check and check < 4 : cnt += check
            if check == 0 and val == 4 : val = 1
            val = int(val)
            if check > 0 and val == 1 : val = 1.001
            line.append(val)
        ret.append(line)
    return ret, cnt    

def solution(arr):
    cnt = 0
    while True :
        if len(arr) == 1 : break 
        arr, cnt = quadfy(arr, cnt)
    return [cnt,int(arr[0][0])]