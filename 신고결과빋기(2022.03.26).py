def solution(id_list, report, k):
    answer = []
    dic1 = dict() # 누구를 신고했는지 저장
    dic2 = dict() # 몇 번 신고 당했는지 저장
    report = list(set(report))
    for i in range(len(id_list)):
        dic1[id_list[i]] = []
        dic2[id_list[i]] = 0
    for i in range(len(report)):
        a, b = report[i].split()
        dic1[a].append(b)
        dic2[b] += 1
    for i in range(len(id_list)):
        t = 0
        for j in dic1[id_list[i]]:
            t += 1 if dic2[j] >= k else 0
        answer.append(t)
    return answer