class Point:
    """A class to represent a point.
    """
    count = 0
    def __init__(self, name, x0, y0):
        self.name = name
        self.x = x0
        self.y = y0
        Point.count+=1

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod  # Decerator gets rid of need for self parameter in get_count
    def get_count():
        return Point.count

    def __str__(self):
        return "The point {0} is at [{1}, {2}]".format(self.name, self.x, self.y)

    def __add__(self,p2):
        return Point(self.name+'-plus-'+p2.name,self.x+p2.x,self.y+p2.y)

    def __sub__(self,p2):
        return Point(self.name+'-minus-'+p2.name,self.x-p2.x,self.y-p2.y)

# create some points
p1 = Point('point-1', 100, 200)
p2 = Point('point-2', 110, 210)
p3 = Point('point-3', 120, 220)


p1.move_by(1, 1)
p2.move_by(1, 1)
p3.move_by(1, 1)

# p1.display()
# p2.display()
# p3.display()

p4 = p1 - p2
# p4.display()
print p4
print Point.get_count()