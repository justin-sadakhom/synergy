import enum


class Location(enum.Enum):
    """ Describes whether in or out of Canada """
    domestic = 1
    international = 2
