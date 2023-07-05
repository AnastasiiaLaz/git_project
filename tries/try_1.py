class Airplane:
    def __init__(self, model, seats):
        self.model = model
        self.seats = seats

    def __repr__(self):
        return f"Airplane: {self.model}, {self.seats}"

    def __str__(self):
        return f"{self.seats}"


airplane = Airplane("10A", 44)

print(airplane.model)

airplane_2 = Airplane("10B", 45)

print(airplane_2.model)

print(str(airplane_2))