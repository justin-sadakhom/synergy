from typing import Tuple


def budget_score(supplier_cost: int, budget: Tuple[int, int]) -> float:
    # a = lowest budget
    # b = highest budget
    # x = supplier_cost

    # if the supplier cost is between the budget the buisness is willing to put in, it will return a score with
    # a graph of a/x
    if budget[0] <= supplier_cost <= budget[1]:
        score = budget[0] / supplier_cost

    # if the supplier cost is lower than the budget cost, it will use the graph -(x-a)^2/a + 1
    elif supplier_cost < budget[0]:
        score = -(supplier_cost - budget[0]) ** 2 / budget[0] + 1

    # if the supplier cost is higher than the budget cost, it will use the graph -(x-b)^2/b + (a-1)/b
    else:
        score = -(supplier_cost - budget[1]) ** 2 / budget[1] + (budget[0] - 1) / budget[1]

    # if any score is negative, return 0
    if score < 0:
        score = 0

    return score
