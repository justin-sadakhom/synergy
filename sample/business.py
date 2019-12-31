from typing import List


class Business:
    """ Representation of a business using this program.

    Attributes:
        name: Name of the business.
    """

    def __init__(self, name: str, location: str, ethics: float):

        self.name = name
        self._location = location
        self._ethics_score = ethics

    @property
    def location(self):
        """
        :return: Where the business is located,
                 either 'domestic' or 'international'.
        """
        return self.location

    @location.setter
    def location(self, new_location: str):
        """
        :param new_location: The location to update to.
        :return: The updated location, if successful.
        """
        if new_location != 'domestic' or new_location != 'international':
            raise ValueError('Invalid location!')

        elif self._location == new_location:
            raise ValueError('Location is already ! ' + new_location)

        else:
            self._location = new_location

    @property
    def ethics_score(self):
        """
        :return: How ethical the business is on a scale of 0.0 - 1.0,
                 with 1.0 being most ethical.
        """
        return self._ethics_score

    @ethics_score.setter
    def ethics_score(self, score):
        """
        :param score: The score to update to.
        :return: The updated ethics score, if successful.
        """
        if not isinstance(score, float):
            raise TypeError('Ethics score must be a float!')

        elif not 0.0 <= score <= 1.0:
            raise ValueError('Ethics score must be between 0.0 and 1.0,'
                             ' inclusive!')

        else:
            self._ethics_score = float(score)
