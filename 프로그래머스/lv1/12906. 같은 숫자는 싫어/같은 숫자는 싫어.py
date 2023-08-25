def solution(arr):
    answer = []
    while arr :
        e = arr.pop()
        if len(answer) == 0 or answer[-1] != e : answer.append(e)
    return answer[::-1] 