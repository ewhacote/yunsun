def solution(picks, minerals):
    # minerals를 5개씩 자르기
    minerals_divided = list_divided(minerals, 5)

    costs = []
    for section in minerals_divided:
        cost = [0, 0, 0]
        for mineral in section:
            if mineral == "diamond": 
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mineral == "iron": 
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else: 
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
    else:
        while len(costs) > sum(picks): 
            costs.pop()

    costs_sorted = sorted(costs, key=lambda x: x[2], reverse=True)
    cost_integrated = 0
    for cost in costs_sorted:
        if picks[0] > 0:
            cost_integrated += cost[0]
            picks[0] -= 1
            continue

        if picks[1] > 0:
            cost_integrated += cost[1]
            picks[1] -= 1
            continue

        if picks[2] > 0:
            cost_integrated += cost[2]
            picks[2] -= 1

    return cost_integrated


def list_divided(target_list: list, n: int):
    return [target_list[i:i+n] for i in range(0, len(target_list), n)]