class Wall:
    def __init__(self, string):
        info = [int(x) for x in string.split()]
        self.x = info[0]
        self.y = info[1]
        self.r = info[2]

    def __lt__(self, other_wall):
        return self.x - self.r < other_wall.x - other_wall.r 

    def __eq__(self, other_wall):
        return self.x == other_wall.x and self.y == other_wall.y and self.r == other_wall.r

    def __contains__(self, circle):
        return circle.is_inside(self)

    def is_inside(self, another):
        if self.r > another.r:
            raise ValueError('The circle should be smaller!')

        is_x_inside = another.x - another.r < self.x < another.x + another.r 
        is_y_inside = another.y - another.r < self.y < another.y + another.r 

        if is_x_inside and is_y_inside:
            return True
        else:
            return False
