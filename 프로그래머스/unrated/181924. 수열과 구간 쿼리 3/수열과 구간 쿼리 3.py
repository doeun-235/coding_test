def solution(arr, queries):
    idx = list(range(len(arr)))
    for call in queries :
        idx [call[0]], idx[call[1]] = idx[call[1]], idx[call[0]]
    return list(map(lambda x:arr[x],idx))