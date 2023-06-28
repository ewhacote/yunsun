def solution(sequence, k):
    answer = []
    # 뒤에서 부터 빼는데, 만약 빼다가 마이너스가 되면 맨 뒤에꺼는 다시 더해준다.
    temp = k
    seq_len = len(sequence)
    j = seq_len - 1
    temp_seq_len = seq_len
    
    while True:
        if temp == 0:
            while sequence[j] == sequence[temp_seq_len - 1]:
                answer.extend([temp_seq_len - 1, j - 1])
                break
            answer.extend([temp_seq_len, j])
            break
        elif temp < 0:
            temp += sequence[j]
            j -= 1
        temp -= sequence[temp_seq_len - 1]
        temp_seq_len -= 1

    
    return answer