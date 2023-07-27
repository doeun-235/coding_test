def solution(array, commands):
    answer = []
    for call in commands:
        answer.append(sorted(array[call[0]-1:call[1]])[call[2]-1])
    return answer