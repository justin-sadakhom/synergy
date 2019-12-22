from sample.business import Business


class Supplier(Business):
    """ Suppliers seek to supply their product to a Client.

    Attributes:
        material: the product the supplier is able to provide
        cost: cost of the materials
        delivery_time: how long it takes to transport material, in days
    """

    def __init__(self, name: str, location: str, ethics: float,
                 material: str, cost: int, delivery_time: int):

        super().__init__(name, location, ethics)
        self.cost = cost
        self.material = material
        self.delivery_time = delivery_time
