class MotarVehicle:
    def __init__(self, range):
        self.range = range
        self.tank = range

    def travel(self, distance):
        if distance > self.tank:
            print("Not Enough")
            self.tank = 0
        else:
            print(f"VOOM ! travelled {distance} kms !!")

    def refuel(self):
        print("Refueling....")
        self.tank = self.range

    def __str__(self):
        return f" Vehicle(range= {self.range}, tank={self.tank})"


class Car(MotarVehicle):
    def __init__(self, range, wheels, color):
        super().__init__(range)
        self.wheels = wheels
        self.color = color


# Creating Class
mv = MotarVehicle(999)

print(mv)
mv.travel(400)
print(mv)

print(mv.travel(10000))
c = Car(500, 4, 'Blue')
print(c.range, c.tank, c.wheels, c.color)
