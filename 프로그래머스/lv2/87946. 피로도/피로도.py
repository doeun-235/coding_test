def go_dungeon(ftg,dungeons,pos,visited,answer):
    if ftg >= pos[1] :
        visited = visited + [pos]
        ftg -= pos[2]
        for next in dungeons:
            if next in visited : continue
            answer = go_dungeon(ftg,dungeons,next,visited,answer)
    return len(visited) if (answer < len(visited)) else answer

def solution(k, dungeons):
    answer = -1
    dungeons = [[i]+data for i,data in enumerate(dungeons)]
    for start in dungeons :
        answer = go_dungeon(k,dungeons,start,[],answer)
        if answer == len(dungeons) : return answer
    return answer