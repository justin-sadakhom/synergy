from sample.client import Client
from sample.supplier import Supplier


class Pair:
    """ Represents a potential pairing between Client and Supplier.

    Attributes:
        client: the Client object
        supplier: the Supplier object
    """

    PERFECT_SCORE = 1.0

    def __init__(self, client: Client, supplier: Supplier):

        self.client = client
        self.supplier = supplier

    # Sum up all the weighted scores
    def synergy_score(self) -> float:

        # Will have more than delivery_score() as we add more functions
        return self.delivery_score() * 0.15 + budget_score() * 0.30 + location_score()*0.1

    def delivery_score(self) -> float:

        max_late_days = 5
        perfect_score = self.PERFECT_SCORE
        expected_time = self.client.delivery_time
        actual_time = self.supplier.delivery_time

        if actual_time <= expected_time:
            return perfect_score

        # Results in score of 0 if order is late by max_late_days days
        else:
            return perfect_score - (actual_time - expected_time) / max_late_days

    def location_score(self) -> float:
        #gets client and supplier location and compares them
        client_location = self.client.location(self.client)
        supplier_location = self.supplier.location(self.supplier)
        perfect_score = self.PERFECT_SCORE

        if client_location == supplier_location:
            return perfect_score

        else:
            # 0.75 is penalty
            return perfect_score * 0.75

    def ethics_score(self) -> float:

        # need to discuss weight for ethics
        supplier_ethic_score = self.supplier.ethics_score(self.supplier)
        return supplier_ethic_score

    def budget_score(self) -> float:
        # a = lowest budget
        # b = highest budget
        # x = supplier_cost

        min_budget = self.client.budget[0]
        supplier_cost = self.supplier.cost
        max_budget = self.client.budget[1]

        # if the supplier cost is between the budget the buisness is willing to put in, it will return a score with
        # a graph of a/x
        if min_budget <= sup_cost <= max_budget:
            score = min_budget / supplier_cost

        # if the supplier cost is lower than the budget cost, it will use the graph -(x-a)^2/a + 1
        elif supplier_cost < min_budget:
            score = -(supplier_cost - min_budget) ** 2 / min_budget + 1

        # if the supplier cost is higher than the budget cost, it will use the graph -(x-b)^2/b + (a-1)/b
        else:
            score = -(supplier_cost - max_budget) ** 2 / max_budget + (min_budget - 1) / max_budget[1]

        # if any score is negative, return 0
        if score < 0:
            score = 0
        elif score > self.PERFECT_SCORE:
            score = 1

        return score
