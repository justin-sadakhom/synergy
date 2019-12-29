from sample.business import Business


class Supplier(Business):
    """ Suppliers seek to supply their product to a Client.

    Attributes:
        material: The product the supplier is able to provide.
        cost: Cost of the materials.
        delivery_time: How long it takes to transport material, in days.
    """

    def __init__(self, name: str, location: str, ethics: float, quantity: int,
                 material: str, cost: int, delivery_time: int):

        super().__init__(name, location, ethics, [quantity])
        self.cost = cost
        self.material = material
        self.delivery_time = delivery_time
