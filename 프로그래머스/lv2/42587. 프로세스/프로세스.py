from collections import deque

def solution(priorities, location):
    jobs = deque(list(range(len(priorities))))
    visited = set()
    prior_dict = {i:priorities[i] for i in range(len(priorities))}
    while jobs:
        job = jobs.popleft()
        if job in visited : continue
        if prior_dict[job] >= max(prior_dict.values()) :
            visited.add(job)
            if job == location : break
            del prior_dict[job]
        else : jobs.append(job)
    return len(visited)