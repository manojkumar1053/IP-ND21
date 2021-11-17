class MagicShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return f"MagicShoppingCart({self.items})"

    def __contains__(self, item):
        return item.lower() in self.items


cart = MagicShoppingCart({
    "Apples".lower(): 20,
    "bananas".lower(): 27,
    "oranges".lower(): 17
})

print(len(cart))
print(cart)
print("Apples" in cart)
print("grapes" in cart)
