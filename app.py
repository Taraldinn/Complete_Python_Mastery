class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        cls = (0, 0)
        

    def draw(self):
        print(f"Point ({self.x} , {self.y})")


point = Point(1, 2)
print(point.default_color)
point.draw()


point = Point.zero()
another.draw()


