def solution(n, lost, reserve):
    reserve_modi = list(set(reserve) - set(lost))
    lost_modi = list(set(lost) - set(reserve))

    for i in reserve_modi:
        if i - 1 in lost_modi:
            lost_modi.remove(i-1)
        elif i + 1 in lost_modi:
            lost_modi.remove(i+1)
    return n - len(lost_modi)