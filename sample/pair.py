from sample.client import Client
from sample.supplier import Supplier


class Pair:
    """ Represents a potential pairing between Client and Supplier.
    """
    
    PERFECT_SCORE = 1.0
    DELIVERY_WEIGHT = 0.15
    BUDGET_WEIGHT = 0.25
    QUANTITY_WEIGHT = 0.25
    QUALITY_WEIGHT = 0.2
    LOCATION_WEIGHT = 0.1
    ETHICS_WEIGHT = 0.05
    BAD_LOCATION_PENALTY = 0.75
    PERFECT_QUALITY_RATING= 5.0

    def __init__(self, client: Client, supplier: Supplier):
        """ Default constructor.

        :Args:
            :param client: The Client object.
            :param supplier: The Supplier object.
        """

        self.client = client
        self.supplier = supplier

    def synergy_score(self) -> float:
        """ Calculate how compatible the Client and Supplier are,
            based on the needs of each.

        :return: Sum of all the weighted scores.
        """

        delivery_weight = self.DELIVERY_WEIGHT
        budget_weight = self.BUDGET_WEIGHT
        location_weight = self.LOCATION_WEIGHT
        ethics_weight = self.ETHICS_WEIGHT
        quality_weight = self.QUALITY_WEIGHT

        return (self.delivery_score() * delivery_weight +
                self.budget_score() * budget_weight +
                self.location_score() * location_weight +
                self.ethics_score() *ethics_weight +
                self.quality_score()*quality_weight)

    def delivery_score(self) -> float:
        """ Calculate a score based on punctuality of Supplier's delivery.

        :return: A delivery score.
        """

        max_late_days = 5
        perfect_score = self.PERFECT_SCORE
        expected_time = self.client.delivery_time
        actual_time = self.supplier.delivery_time

        if actual_time <= expected_time:
            return perfect_score

        # Results in score of 0 if order is late by max_late_days days
        return perfect_score - (actual_time - expected_time) / max_late_days

    def location_score(self) -> float:
        """ Calculate a score based on the Client's preferred location and the
            location of the Supplier.

        :return: A location score.
        """

        client_location = self.client.location(self.client)
        supplier_location = self.supplier.location(self.supplier)
        perfect_score = self.PERFECT_SCORE
        bad_location_penalty = self.BAD_LOCATION_PENALTY

        if client_location == supplier_location:
            return perfect_score

        return perfect_score * bad_location_penalty
    def quality_score(self) -> float:
        """Calculate a score based on quality of material

        :return: A quality score
        """

        material_quality_rating = self.supplier.quality
        perfect_quality_rating = self.PERFECT_QUALITY_RATING
        quality_score = material_quality_rating/perfect_quality_rating

        return quality_score

    def ethics_score(self) -> float:
        """ Calculate a score based on the reputation of Supplier's ethics.

        :return: An ethics score.
        """

        # Need to discuss weight for ethics
        supplier_ethic_score = self.supplier.ethics_score(self.supplier)

        return supplier_ethic_score

    def budget_score(self) -> float:
        """ Calculate a score based on the budget of the Client and the cost of
        the supplies that Supplier is offering.

        Abbreviations:
            a: lowest budget
            b: highest budget
            x: supplier_cost

        :return: A budget score.
        """

        min_budget = self.client.budget[0]
        supplier_cost = self.supplier.cost
        max_budget = self.client.budget[1]

        # Cost is within budget, use the function a / x
        if min_budget <= supplier_cost <= max_budget:
            score = min_budget / supplier_cost

        # Cost lower than budget, use the function -(x - a)^2 / a + 1
        elif supplier_cost < min_budget:
            score = -(supplier_cost - min_budget) ** 2 / min_budget + 1

        # Cost higher than budget, use the function -(x - b)^2 / b + (a - 1) / b
        else:
            score = -(supplier_cost - max_budget) ** 2 / max_budget + (
                    min_budget - 1) / max_budget[1]

        # if any score is negative, return 0
        if score < 0:
            score = 0

        elif score > self.PERFECT_SCORE:
            score = 1

        return score
