class House:
    PRICE_PER_SQUARE_FOOT = 2.5

    def __init__(self, size, num_bedrooms=1):
        self.size = size
        self.num_bedrooms = num_bedrooms

    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT

    @price.setter
    def price(self,new_price):
        self.size = new_price/self.PRICE_PER_SQUARE_FOOT

home = House(999)

#print(home.price())
print(home.size)
print(home.price)

home.price = 99
# Using setter decorator to set the price
print(home.size)


