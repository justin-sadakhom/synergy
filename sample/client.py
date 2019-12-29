from typing import List, Tuple
from sample.business import Business


class Client(Business):
    """ Clients seek a partnership with a Supplier.

    Attributes:
        budget: How much the client is willing to spend, in dollars,
                formatted as a Tuple expressing a range of (min, max).
        materials: What materials the client is seeking.
        delivery_time: Estimated time client wants their order fulfilled by.
    """

    def __init__(self, name: str, location: str, ethics: float, quantity: List[int],
                 budget: Tuple[int], materials: List[str], delivery_time: int):

        super().__init__(name, location, ethics, quantity)
        self.budget = budget
        self.materials = materials
        self.delivery_time = delivery_time
