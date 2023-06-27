def solution(targets):
    # 제일 e가 작은 순으로 정렬하고 가장 작은 e 구하기 
    s = []
    e = []
    
    for idx, target in enumerate(targets):
        s.append(target[0])
        e.append(target[1])
    
    sorted_s = sorted(s)
    sorted_e = sorted(e)
    
    min_e = sorted_e[1]
    
    # 첫번째 미사일은 무조건 x = min_e - 0.5
    intercept = []
    x = min_e - 0.5
    intercept.append(x)
    
    # 그다음에 첫 번째 e - 0.5 한테 관통당한 애들을 제외한다
    # 즉 s가 e 이상(또는 e - 0.5 초과)인 애 중 가장 작은 s를 구한다
    next_s = s[0]
    i = 0
    while next_s < (min_e - 0.5):
        i++
        next_s = s[i]
    
    # 나머지 e들 중에서 가장 작은 애를 선택, 두번째 미사일은 x = min(e) - 0.5 반복
    
    
    
    
    
    answer = 0
    return answer