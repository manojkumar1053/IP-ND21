class House:
    PRICE_PER_SQ_FOOT = 2.5

    def __init__(self, size):
        self.size = size

    @property
    def price(self):
        return self.size * self.PRICE_PER_SQ_FOOT

    @price.setter
    def price(self, new_price):
        self.size = new_price / self.PRICE_PER_SQ_FOOT


home = House(10000)
print(home.size)
print(home.price)
