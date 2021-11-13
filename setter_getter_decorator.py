class Distance:
    _KM_PER_MILE = 1.60934

    def __init__(self, km):
        self.km = km

    @property
    def miles(self):
        return self.km / self._KM_PER_MILE

    @miles.setter
    def miles(self, miles):
        self.km = miles * self._KM_PER_MILE


d = Distance(1000)
d.miles = 500
