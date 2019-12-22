from sample.client import  Client
from sample.supplier import Supplier

""" Example initialization of objects
"""

S1 = Supplier('Crystal', 'international', 0.5, 'poison', 15000, 1)
S2 = Supplier('Amanda', 'international', 0.5, 'poison', 19000, 2)
S3 = Supplier('Alison', 'domestic', 0.5, 30000, 3)

suppliers = [S1, S2, S3]

C1 = Client("Yug's Bugs", 'international', 1.0, (15000, 20000), ['poison'], 1)
