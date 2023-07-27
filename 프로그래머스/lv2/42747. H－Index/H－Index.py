def solution(citations):
    citations = sorted(citations,key=lambda x : -x)
    for i,val in enumerate(citations):
        if val < i+1 : return i
    else : return len(citations)