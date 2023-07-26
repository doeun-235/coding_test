ways =[(0,1),(1,0),(0,-1),(-1,0)]
way_gone = {way : False for way in ways}

def grid2board(grid):
    return [list(line) for line in grid]

def change_way(way,s):
    ind = ways.index(way)
    if s == 'S' : return way
    elif s == 'L' : return ways[(ind-1)%4]
    else : return ways[(ind+1)%4]

def go_cycle(board,x,y,way,passed):
    n, m = len(board[0]),len(board)
    cycle_len = 1
    pos_x,pos_y = x,y
    passed[(pos_x,pos_y)][way] = True
    new_way=way
    while True:
        pos_x,pos_y = (pos_x+new_way[0])%m,(pos_y+new_way[1])%n
        new_way=change_way(new_way,board[pos_x][pos_y])
        passed[(pos_x,pos_y)][new_way] = True
        if (pos_x,pos_y)==(x,y) and new_way == way : break
        cycle_len += 1
    return cycle_len,passed
        
def solution(grid):
    answer = []
    board = grid2board(grid)
    n, m = len(board[0]),len(board)
    passed = {(j,i) : {way: False for way in ways} for i in range(n) for j in range(m)}
    for x in range(m):
        for y in range(n):
            for way in ways:
                if passed[(x,y)][way] : continue
                cycle_len,passed = go_cycle(board,x,y,way,passed)
                answer.append(cycle_len)
    return sorted(answer)