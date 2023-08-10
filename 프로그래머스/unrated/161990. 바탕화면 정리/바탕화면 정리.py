def find_file(line):
    check = list(map(lambda x: x== '#',line))
    nums = list(zip(check,range(len(line))))
    ret = []
    for c, n in nums:
        if c : ret.append(n)
    return ret     

def solution(wallpaper):
    lux,luy,rdx,rdy = 52,52,-1,-1
    for ind,line in enumerate(wallpaper):
        files = find_file(line)
        if not len(files): continue
        if ind < lux : lux = ind
        if files[0] < luy : luy = files[0]
        if rdx < ind+1 : rdx = ind+1
        if rdy < files[-1]+1 : rdy = files[-1]+1
    return lux,luy,rdx,rdy 