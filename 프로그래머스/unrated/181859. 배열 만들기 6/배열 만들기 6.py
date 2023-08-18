def solution(arr):
    answer = []
    for a in arr :
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
        else : answer.pop()
    return answer if answer else [-1]