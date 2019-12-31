from typing import List
from sample.business import Business


class Supplier(Business):
    """ Suppliers seek to supply their product to a Client.

    Attributes:
        cost: Cost of the materials.
        delivery_time: How long it takes to transport material, in days.
        quality: Ability to satisfy customers, rated on a scale of 0.0 to 5.0.
    """

    def __init__(self, name: str, location: str, ethics: float,
                 materials: List[str], quantity: List[int],
                 cost: int, delivery_time: int, quality: List[float]):

        super().__init__(name, location, ethics, materials, quantity)
        self.cost = cost
        self.delivery_time = delivery_time
        self.quality = quality
