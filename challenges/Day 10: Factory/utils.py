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
    h = machine.heuristic_value(initial)
    queue = [(h, 0, initial)]
    visited = set([tuple(initial)])

    while queue:
        h, g, state = heapq.heappop(queue)
        if (machine.won(state)): return g

        for button in machine.valid_buttons(state):
            n_state = machine.apply2(state, button)
            if n_state not in visited:
                visited.add(n_state)
                heapq.heappush(queue, (g + 1 + machine.heuristic_value(n_state), g + 1, n_state))
            # undo

    return float('inf')

class Machine(object):
    def __init__(self, goal, buttons, joltages):
        self.goal = goal; self.buttons = tuple(buttons); self.joltages = tuple(joltages)

    def key(self, state): return ''.join(list(map(lambda x: '#' if x else '.', state)))

    def apply(self, state, button):
        result = state.copy()
        for pos in button: result[pos] = not result[pos]
        return result
    
    def apply2(self, state, button):
        return tuple([ state[pos] + (1 if pos in button else 0) for pos in range(len(state))])
    
    def heuristic_value(self, joltages):
        res = 0
        for i in range(len(joltages)): res += self.joltages[i] - joltages[i]
        return res
    
    def won(self, state):
        for i in range(len(state)):
            if state[i] != self.joltages[i]: return False
        return True
    
    def can_increase_apply_button_joltage(self, state, button):
        for pos in button:
            if state[pos] == self.joltages[pos]: return False
        return True
    
    def valid_buttons(self, state):
        res = []
        for button in self.buttons:
            if self.can_increase_apply_button_joltage(state, button): res.append(button)
        return res
    
    def fewest_required_buttons(self): return bfs_lights(self)
    def fewest_required_joltage_buttons(self): return bfs_joltage(self)