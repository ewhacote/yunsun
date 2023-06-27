from math import ceil, floor

def solution(r1, r2):
    # 제 1사분면 위의 점의 갯수를 구하기
    # 일단 두개
    answer = 0
    
    for i in range(1, r2 + 1):
        # 반지름 제곱해서 가로 제곱을 빼고 루트 씌워서 세로 확인
        # 이 두개 사이에 정수가 있는지.. 어떻게 확인하지
        big_y = floor((r2**2 - i**2)**(1/2))
        if i >= r1:
            small_y = 0
            answer += floor(big_y - small_y) + 1
        else:
            small_y = ceil((r1**2 - i**2)**(1/2))
            if type(big_y) is int or type(small_y) is int:
                answer += floor(big_y - small_y) + 1
            else:
                answer += floor(big_y - small_y)
    
    # 제 1사분면 위의 점의 갯수에 4 곱하기
    answer *= 4

    return answer