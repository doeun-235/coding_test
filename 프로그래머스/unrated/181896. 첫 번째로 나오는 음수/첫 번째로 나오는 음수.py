def solution(num_list):
    sign = list(map(lambda x : x < 0, num_list))
    try : return sign.index(True)
    except : return -1