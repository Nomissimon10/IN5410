import random


class Appliance:
    def __init__(self, name: str, duration: float, min: int, max: int, energy_consumption_w: int, energy_consumption_w_max: int = None):
        self.name = name
        self.duration = float(duration)
        self.min = min
        self.max = max
        if energy_consumption_w_max is None:
            self.consumes = energy_consumption_w
        else:
            self.consumes = self.randomize_usage_between(
                energy_consumption_w, energy_consumption_w_max)

    def randomize_usage_between(self, min: int, max: int):
        return random.randint(min, max)

    def __str__(self):
        return f"{self.name} ({self.energy_consumption}W, {self.hours}h, {self.min}-{self.max})"


standard_appliances = [
    Appliance("Lighting", 10, 10, 20, 1000, 2000),
    Appliance("Heating", 24, 0, 24, 6400, 9600),
    Appliance("Refrigerator/Freezer", 24, 0, 24, 1320, 3960),
    Appliance("Electric Stove", 24, 7, 22, 3900),
    Appliance("TV", 5, 12, 23, 150, 600),
    Appliance("Computers", 6, 7, 23, 1200),  # Two computers
]

shiftable_appliances = [
    Appliance("Diswasher", 2, 23, 10, 1440),
    Appliance("Laundry Machine", 1.5, 23, 10, 1940),
    # From 16:00 after work to 07:00 in the morning before work
    Appliance("Electric Vehicle", 4, 16, 7, 9900),
]
