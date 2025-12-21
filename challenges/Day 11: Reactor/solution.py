input_path = 'challenges/Day 11: Reactor/input'

graph, starting, ending = {}, 'you', 'out'
with open(input_path) as f:
  for line in f:
    line = line[:-1].split(' ')
    node = line[0][:-1]
    graph[node] = line[1:]

def paths(graph, current, target, memo={}):
    if current == target: return 1
    if current not in graph: return 0

    if current not in memo:
        memo[current] = sum(paths(graph, neighbor, target, memo) for neighbor in graph[current])
    
    return memo[current]

print('Part 1:', paths(graph, starting, ending))