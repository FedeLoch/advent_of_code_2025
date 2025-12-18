from collections import deque
import heapq

def bfs_lights(machine):
    # Using bfs to find minimum button presses for lights
    current = machine.goal
    queue = deque([(current, 0)])
    visited = set([machine.key(current)])

    while queue:
        state, steps = queue.popleft()
        if not any(state): return steps

        for button in machine.buttons:
            next_state = machine.apply(state, button)
            next_key = machine.key(next_state)
            if next_key not in visited:
                visited.add(next_key)
                queue.append((next_state, steps + 1))

    return float('inf')

def bfs_joltage(machine):
    # Using A* to find minimum button presses for joltages
    initial = [0] * len(machine.joltages)
    h = sum(machine.joltages[i] - initial[i] for i in range(len(initial)))
    queue = [(h, 0, initial)]
    visited = set([tuple(initial)])

    while queue:
        _, g, state = heapq.heappop(queue)
        if all(state[i] == machine.joltages[i] for i in range(len(state))): return g

        for button in machine.valid_buttons(state):
            next_state = state.copy()
            for pos in button: next_state[pos] += 1
            next_key = tuple(next_state)
            if next_key not in visited:
                visited.add(next_key)
                h_new = sum(machine.joltages[i] - next_state[i] for i in range(len(next_state)))
                heapq.heappush(queue, (g + 1 + h_new, g + 1, next_state))

    return float('inf')

class Machine(object):
    def __init__(self, goal, buttons, joltages):
        self.goal = goal; self.buttons = buttons; self.joltages = joltages

    def key(self, state): return ''.join(list(map(lambda x: '#' if x else '.', state)))

    def apply(self, state, button):
        result = state.copy()
        for pos in button: result[pos] = not result[pos]
        return result
    
    def valid_buttons(self, state):
        return [button for button in self.buttons if not any(state[pos] + 1 > self.joltages[pos] for pos in button)]
    
    def fewest_required_buttons(self):
        return bfs_lights(self)
    
    def fewest_required_joltage_buttons(self):
        return bfs_joltage(self)