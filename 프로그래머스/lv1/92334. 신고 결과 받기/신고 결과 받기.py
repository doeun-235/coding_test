def solution(id_list, report, k):
    report_dict= {id:[] for id in id_list}
    reported_dict = {id:0 for id in id_list}
    banned_dict = {id:False for id in id_list}
    
    report = list(set(report))
    
    for line in report:
        user1,user2=line.split(' ')
        report_dict[user1].append(user2)
        if reported_dict[user2] == k-1:
            banned_dict[user2] = True
        reported_dict[user2] += 1
        
    return [len(list(
        filter(lambda x : banned_dict[x],report_dict[id]))
               ) for id in id_list]