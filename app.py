class Point:
    @staticmethod
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
