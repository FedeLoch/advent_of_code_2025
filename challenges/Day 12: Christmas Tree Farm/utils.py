
class Shape(object):
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid
        self.cells = []
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char == '#':
                    self.cells.append((r, c))

class Region(object):
    def __init__(self, dimensions, requirements):
        self.dimensions = dimensions; self.requirements = requirements

    def is_satisfiable(self, shapes):
        region_area = self.dimensions[0] * self.dimensions[1]
        required_area = 0
        for shape_id, count in self.requirements:
            shape = shapes[shape_id]
            shape_area = len(shape.cells)
            required_area += count * shape_area
            
        return required_area <= region_area