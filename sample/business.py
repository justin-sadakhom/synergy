class Business:
    """ Representation of a business using this program.

    Attributes:
        name: name of the business
        location: where the business is located
    """

    def __init__(self, name: str, location: str, ethics: float) -> None:

        self.name = name
        self.location = location
        self._ethics_score = ethics
    
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
