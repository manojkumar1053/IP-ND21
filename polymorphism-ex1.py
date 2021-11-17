class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p = Point()
print(p)
a = Point(3, 5)
print(a)
print(a + Point(5, 9))
print(a)
