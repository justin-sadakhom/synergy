from typing import List, Tuple
from sample.business import Business


class Client(Business):
    """ Clients seek a partnership with a Supplier.

    Attributes:
        budget: how much the client is willing to spend, in dollars,
                formatted as a Tuple expressing a range of (min, max)
        materials: what materials the client is seeking
        delivery_time: estimated time client wants their order fulfilled by
    """

    def __init__(self, budget: Tuple[int], materials: List[str],
                 delivery_time: int):

        self.budget = budget
        self.materials = materials
        self.delivery_time = delivery_time
