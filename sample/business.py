class Business:
    """ Representation of a business using this program.

    Attributes:
        name: name of the business
    """

    def __init__(self, name: str, location: str, ethics: float):

        self.name = name
        self.location = location
        self._ethics_score = ethics

    @property
    def location(self):
        """
        :return: where the business is located
                 either 'domestic' or 'international'
        """
        return self.location

    @location.setter
    def location(self, new_location: str):

        if new_location != 'domestic' or new_location != 'international':
            raise ValueError('Invalid location!')

        elif self.location == new_location:
            raise ValueError('Location is already ! ' + new_location)

        else:
            self.location = new_location

    @property
    def ethics_score(self):
        """
        :return: how ethical the business is on a scale of 0.0 - 1.0,
                 with 1.0 being most ethical
        """
        return self._ethics_score

    @ethics_score.setter
    def ethics_score(self, score):

        if not isinstance(score, float):
            raise TypeError('Ethics score must be a float!')

        elif not 0.0 <= score <= 1.0:
            raise ValueError('Ethics score must be between 0.0 and 1.0,'
                             ' inclusive!')

        else:
            self._ethics_score = float(score)
