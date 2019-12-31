from typing import Tuple
from sample.business import Business
from sample.request import Request


class Client(Business):
    """ Clients seek a partnership with a Supplier.

    Attributes:
        requests: The type of products the Client is seeking.
    """

    def __init__(self, name: str, location: str, ethics: float,
                 budget: Tuple[int, int]):

        super().__init__(name, location, ethics,)
        self.budget = budget
        self.requests = []

    def add_request(self, request: Request):

        if request not in self.requests:
            self.requests.append(request)
