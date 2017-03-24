class Wall:
    def __init__(self, string):
        info = [int(x) for x in string.split()]
        self.x = info[0]
        self.y = info[1]
        self.r = info[2]

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.r)
    
    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.r)

    def __lt__(self, other_wall):
        #return self.x - self.r < other_wall.x - other_wall.r 
        return self.r < other_wall.r 

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

class Fortress:
    def __init__(self, N):
        self.walls = list()
        for _ in range(N):
            self.walls.append(Wall(input()))
        self.walls.sort(reverse=True)

class Node:
    def __init__(self, string):
        self.wall = Wall(string)
        self.inside_walls = list()

    def __repr__(self):
        if not self.inside_walls:
            return str(self.wall)
        else:
            return "%s - %s" % (self.wall, self.inside_walls)

    def add_child(self, string):
        wall = Wall(string)
        if not self.inside_walls:
            self.inside_walls.append(Node(string))
            return 1

        for child in self.inside_walls:
            if wall in child.wall:
                return 1 + child.add_child(string)
        
        self.inside_walls.append(Node(string))
        return 1

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        fortress = Fortress(N)

if __name__ == '__main__':
    main()
