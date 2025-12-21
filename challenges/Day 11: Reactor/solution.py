input_path = 'challenges/Day 11: Reactor/input'

graph = {}
with open(input_path) as f:
  for line in f:
    line = line[:-1].split(' ')
    node = line[0][:-1]
    graph[node] = line[1:]

def count_paths(graph, current, target, memo=None):
    if memo is None: memo = {}
    if current == target: return 1
    if current not in graph: return 0
    
    if current not in memo:
        memo[current] = sum(count_paths(graph, neighbor, target, memo) for neighbor in graph[current])
    
    return memo[current]

# Part 1
print('Part 1:', count_paths(graph, 'you', 'out'))

# Part 2
# Check order: dac -> fft or fft -> dac
dac_to_fft = count_paths(graph, 'dac', 'fft')
fft_to_dac = count_paths(graph, 'fft', 'dac')

if dac_to_fft > 0:
    # Path: svr -> dac -> fft -> out
    p1 = count_paths(graph, 'svr', 'dac')
    p2 = dac_to_fft
    p3 = count_paths(graph, 'fft', 'out')
    print('Part 2:', p1 * p2 * p3)
elif fft_to_dac > 0:
    # Path: svr -> fft -> dac -> out
    p1 = count_paths(graph, 'svr', 'fft')
    p2 = fft_to_dac
    p3 = count_paths(graph, 'dac', 'out')
    print('Part 2:', p1 * p2 * p3)
else:
    print('Part 2: 0')
