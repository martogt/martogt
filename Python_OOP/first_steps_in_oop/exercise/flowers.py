class Flower:
    is_happy = False

    def init(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
