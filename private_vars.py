class House:
    __PRICE_PER_SQ_FOOT = 2.5

    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self.size * self.__PRICE_PER_SQ_FOOT

    @price.setter
    def price(self, new_price):
        self.size = new_price / self.__PRICE_PER_SQ_FOOT


home = House(10000)
print(home.size)
print(home.price)

print(House.__dict__)

for k,v in House.__dict__.items():
    print(k,": ",v)
