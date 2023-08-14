def find_cha(board,s):
    ans = set() 
    for i,line in enumerate(board) :
        for j,x in enumerate(line) :
            if x == s : ans.add((i,j))
    return ans

def check_line(p_set):
    if len(p_set) < 3 : return 0 
    ans, line_type = 0, set()
    for i in range(3):
        if set([(i,0),(i,1),(i,2)]).issubset(p_set) :
            ans += 1
        if set([(0,i),(1,i),(2,i)]).issubset(p_set) :
            ans += 1
    if set([(0,0),(1,1),(2,2)]).issubset(p_set) :
        ans += 1
    if set([(0,2),(1,1),(2,0)]).issubset(p_set) :
        ans += 1
    return ans
                                          
def solution(board):
    answer = -1
    O_set, X_set = find_cha(board,'O'), find_cha(board,'X')
    O_len, X_len = len(O_set), len(X_set)
    O_line, X_line = check_line(O_set), check_line(X_set)
    turn_diff = O_len - X_len
    
    if turn_diff == 0 :
        if O_line : return 0
        else : return 1
    elif turn_diff == 1:
        if X_line : return 0
        else : return 1
    else : return 0
    
#    if O_line == 2 :
#        if not X_line and turn_diff == 1 : return 1
#        else : return 0
#    if (O_line + X_line) > 1 : return 0
#    if O_line == 1 and turn_diff == 1: return 1 
#    if X_line == 1 and turn_diff == 0: return 1
#    if not check_line(X_set) and not check_line(O_set):
#        if turn_diff in [0,1] : return 1
#    return 0
