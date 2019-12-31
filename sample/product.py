class Product:
    """ A commodity that a Supplier wants to sell.

    Attributes:
        name: What the product is called.
        quantity: How much is available.
        quality: How well it satisfies customers, on a scale of 0.0 to 5.0.
        cost: Cost per unit, in dollars.
        delivery_time: How long the product takes to ship, in days.
    """

    def __init__(self, name: str, quantity: int, quality: float,
                 cost: int, delivery_time: int):

        self.name = name
        self.quantity = quantity
        self.quality = quality
        self.cost = cost
        self.delivery_time = delivery_time
