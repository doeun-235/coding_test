import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    if scoville[0] >= K : return cnt
    while len(scoville) > 1 :
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+min2*2)
        cnt += 1
        if scoville[0] >= K : return cnt
    else : return -1