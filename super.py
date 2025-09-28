class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"This is a {self.color} shape")

class Circle(Shape):
    def __init__(self, color, radius, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        # super().describe()
        print(f"This is a circle with a radius of {self.radius}")

class Square(Shape):
    def __init__(self, color, width, is_filled):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, height, width, is_filled):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

circle = Circle(color="red", radius=10, is_filled=True)

circle.describe()