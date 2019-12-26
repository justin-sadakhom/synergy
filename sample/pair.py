from sample.client import Client
from sample.supplier import Supplier


class Pair:
    """ Represents a potential pairing between Client and Supplier.

    Attributes:
        client: the Client object
        supplier: the Supplier object
    """

    def __init__(self, client: Client, supplier: Supplier):

        self.client = client
        self.supplier = supplier

    # Sum up all the weighted scores
    def synergy_score(self) -> float:

        # Will have more than delivery_score() as we add more functions
        return self.delivery_score()

    def delivery_score(self) -> float:

        perfect_score = 1.0
        expected_time = self.client.delivery_time
        actual_time = self.supplier.delivery_time

        if actual_time <= expected_time:
            return perfect_score

        else:
            return perfect_score - 0.2(actual_time - expected_time)
