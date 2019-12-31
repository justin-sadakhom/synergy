class Request:
    """ Parameters for a product that a Supplier is seeking.

    Attributes:
        name: What the product is called.
        quantity: How much is available.
        cost: Cost per unit, in dollars.
        delivery_time: How long the product takes to ship, in days.
    """
    def _init__(self, name: str, quantity: int, cost: int, delivery_time: int):

        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.delivery_time = delivery_time
