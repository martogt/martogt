class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * (Circle.__pi * (self.radius ** 2))


# Create a circle with diameter of 10 units
my_circle = Circle(15)

# Calculate the circumference of the circle
circumference = my_circle.calculate_circumference()
print(f"The circumference of the circle is: {circumference:.2f}")

# Calculate the area of the circle
area = my_circle.calculate_area()
print(f"The area of the circle is: {area:.2f}")

# Calculate the area of a sector with a central angle of 60 degrees
sector_area = my_circle.calculate_area_of_sector(5)
print(f"The area of the sector is: {sector_area:.2f}")
