class MagicShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return f"MagicShoppingCart({self.items})"


cart = MagicShoppingCart({
    "Apple": 20,
    "bananas": 27,
    "oranges": 17
})

print(len(cart))
print(cart)
