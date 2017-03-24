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
        if isinstance(other_wall, Wall):
            return self.x == other_wall.x and self.y == other_wall.y and self.r == other_wall.r
        elif isinstance(other_wall, tuple):
            return (self.x, self.y, self.r) == other_wall

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
    def read_string(self, string):
        self.walls = list()
        for line in string.split(sep="\n"):
            self.walls.append(Wall(line))
        self.walls.sort(reverse=True)

    def read_lines(self, N):
        self.walls = list()
        for _ in range(N):
            self.walls.append(Wall(input()))
        self.walls.sort(reverse=True)

    def make_tree(self):
        root = Node(self.walls[0])
        for i in range(1, len(self.walls)):
            this_wall = self.walls[i]
            root.add_child(this_wall)
        return root

class Node:
    def __init__(self, wall):
        self.wall = wall
        self.inside_walls = list()
        self.height = 1

    def __repr__(self):
        if not self.inside_walls:
            return str(self.wall)
        else:
            return "%s - %s" % (self.wall, self.inside_walls)

    def add_child(self, wall):
        if not self.inside_walls:
            self.inside_walls.append(Node(wall))
            self.height = 2
            return

        for child in self.inside_walls:
            if wall in child.wall:
                child.add_child(wall)
                self.height = child.height + 1
                return
        
        self.inside_walls.append(Node(wall))
        return

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        fortress = Fortress(N)

if __name__ == '__main__':
    main()
