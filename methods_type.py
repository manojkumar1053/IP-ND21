class Customer:
    def __init__(self, first_name, surname, tier=('free', 0)):
        self.first_name = first_name
        self.surname = surname
        self._tier = tier[0]
        self._cost = tier[1]

    def bill_for(self, months):
        return months * self._cost

    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @property
    def name(self):
        return f"{self.first_name} {self.surname}"

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, tier=('premium', 10))


marco = Customer('Marco', 'Polo')  # Defaults to the free tier
print(marco.name)  # Marco Polo
print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

james = Customer.premium("James", "Bond")
print(james.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(james.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
print(james.bill_for(5))  # => 50 (5 months at 10$/mo)
print(james.name)  # James Bond
