def solution(numbers, hand):
    answer = ''
    Lpos = [0,3]
    Rpos = [2,3]
    mapper = dict({
        1:[0,0],2:[1,0],3:[2,0],
        4:[0,1], 5:[1,1],6:[2,1],
        7:[0,2],8:[1,2],9:[2,2],
        0:[1,3]
    })
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += "L"
            Lpos = mapper[numbers[i]]
        elif numbers[i] in [3,6,9]:
            answer += "R"
            Rpos = mapper[numbers[i]]
        else:
            if abs((Lpos[0] - mapper[numbers[i]][0])) + abs((Lpos[1] - mapper[numbers[i]][1])) > abs(Rpos[0] - mapper[numbers[i]][0]) + abs(Rpos[1] - mapper[numbers[i]][1]):
                answer += "R"
                Rpos = mapper[numbers[i]]
            elif abs(Lpos[0] - mapper[numbers[i]][0]) + abs(Lpos[1] - mapper[numbers[i]][1]) < abs(Rpos[0] - mapper[numbers[i]][0])  + abs(Rpos[1] - mapper[numbers[i]][1]):
                answer += "L"
                Lpos = mapper[numbers[i]]
            else:
                if hand == "right":
                    answer += "R"
                    Rpos = mapper[numbers[i]]
                else:
                    answer += "L"
                    Lpos = mapper[numbers[i]]
    return answer