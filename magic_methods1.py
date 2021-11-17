class MagicShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return f"MagicShoppingCart({self.items})"

    def __contains__(self, item):
        return item.lower() in self.items

    def __iadd__(self, other):
        for item, count in other.items.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count
        return self


cart = MagicShoppingCart({
    "Apples".lower(): 20,
    "bananas".lower(): 27,
    "oranges".lower(): 17
})

cart2 = MagicShoppingCart({
    "Apples".lower(): 1,
    "bananas".lower(): 1,
    "oranges".lower(): 1
})
print(len(cart))
print(cart)
print("Apples" in cart)
print("grapes" in cart)

cart += cart2
print(cart)
print(len(cart))
print(cart)
print("Apples" in cart)
print("grapes" in cart)
