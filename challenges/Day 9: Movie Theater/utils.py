from collections import deque

def is_valid_rectangle(p1, p2, valid_lines):
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])

    for x in range(xmin, xmax + 1):
        if x not in valid_lines: return False
        _min, _max = valid_lines[x]
        for y in range(ymin, ymax + 1):
            if y < _min or y > _max: return False

    return True

horizotal_points = lambda p1, p2: [ (p1[0], y) for y in range(min(p1[1], p2[1]) + 1, max(p1[1], p2[1])) ]
vertical_points = lambda p1, p2: [ (x, p1[1]) for x in range(min(p1[0], p2[0]) + 1, max(p1[0], p2[0])) ]
all_points_on_line = lambda p1, p2: horizotal_points(p1, p2) if p1[0] == p2[0] else vertical_points(p1, p2)

def build_border(points):
    border, seen = [], set()
    queue = deque([points.pop()])

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen: continue
        seen.add((x, y))
        border.append((x, y))

        for point in points:
            if not point in seen and (point[0] == x or point[1] == y):
                border += all_points_on_line((x, y), point)
                queue.append(point)
    return border

def print_graph(graph):
    for row in graph:
        print(''.join(row))

def add_points_to_graph(points, red_points, filled, graph):
    for x, y in points: graph[y][x] = 'X'
    for x, y in filled: graph[y][x] = 'X'
    for x, y in red_points: graph[y][x] = '#'

    return graph

def border_lines(border):
    _dict = {}
    for x, y in border:
        if x not in _dict: _dict[x] = (y, y); continue
        _dict[x] = (min(_dict[x][0], y), max(_dict[x][1], y))
    return _dict

def valid_tiles(red_points):
    border = build_border(red_points)
    return border_lines(border) # { row -> (min, max) columns }
