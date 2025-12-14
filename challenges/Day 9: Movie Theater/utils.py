from collections import deque

def is_valid_rectangle(p1, p2, valid):
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if (x, y) not in valid: return False

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

# def fill_inside(border):
#     xs = [x for x, _ in border]
#     ys = [y for _, y in border]

#     minx, maxx = min(xs) - 1, max(xs) + 1
#     miny, maxy = min(ys) - 1, max(ys) + 1

#     visited = set()
#     queue = deque([(minx, miny)])

#     while queue:
#         x, y = queue.popleft()
#         if (x, y) in visited: continue
#         if (x, y) in border: continue
#         if not (minx <= x <= maxx and miny <= y <= maxy): continue

#         visited.add((x, y))
#         for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]: queue.append((x+dx, y+dy))

#     inside = set()
#     for x in range(minx+1, maxx):
#         for y in range(miny+1, maxy):
#             if (x, y) not in visited:
#                 inside.add((x, y))

#     return inside

def print_graph(graph):
    for row in graph:
        print(''.join(row))

def add_points_to_graph(points, red_points, filled, graph):
    for x, y in points: graph[y][x] = 'X'
    for x, y in filled: graph[y][x] = 'X'
    for x, y in red_points: graph[y][x] = '#'

    return graph

def valid_tiles(red_points):
    border = build_border(red_points)
    grid = [ [ '.' for i in range(14) ] for i in range(9) ]
    # filled = fill_inside(border)
    print_graph(add_points_to_graph(border, red_points, [], grid))
    return []
