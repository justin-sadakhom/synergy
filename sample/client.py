from typing import List, Tuple
from sample.business import Business


class Client(Business):
    """ Clients seek a partnership with a Supplier.

    Attributes:
        budget: How much the client is willing to spend, in dollars,
                formatted as a Tuple expressing a range of (min, max).
        delivery_time: Estimated time client wants their order fulfilled by.
    """

    def __init__(self, name: str, location: str, ethics: float,
                 materials: List[str], quantity: List[int],
                 budget: Tuple[int], delivery_time: int):

        super().__init__(name, location, ethics, materials, quantity)
        self.budget = budget
        self.delivery_time = delivery_time
