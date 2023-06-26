def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    e = 0
    for t1, t2 in targets:
        if t1 >= e:
            answer += 1
            e = t2
    return answer