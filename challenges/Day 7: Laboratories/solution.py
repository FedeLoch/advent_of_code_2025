input_path = 'challenges/Day 7: Laboratories/input'
from utils import dict_from_file, print_graph

graph = dict_from_file(input_path)

is_valid = lambda pos, graph: 0 <= pos[0] < len(graph) and 0 <= pos[1] < len(graph[0])

def initial_col(graph):
    for c in range(len(graph[0])):
        if graph[0][c] == 'S': return c

def calculate_times(graph, origin):
    queue, result = [origin], 0
    while queue:
        r, c = queue.pop(0)
        if is_valid((r + 1, c), graph):
            if graph[r + 1][c] == '^':
                result += 1; queue.append((r + 1, c - 1)); queue.append((r + 1, c + 1))
            if graph[r + 1][c] == '.':
                graph[r + 1][c] = '|'
                queue.append((r + 1, c))

    return result

print('Part 1:', calculate_times(graph, (0, initial_col(graph))))

print_graph(graph)