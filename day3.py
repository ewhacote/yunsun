def solution(sequence, k):
    answer = []
    l = 0
    s = -1
    temp = 0
    while True:
        if temp < k:
            s += 1
            if s >= len(sequence):
                break
            temp += sequence[s]
        else:
            temp -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if temp == k:
            answer.append([l, s])
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]