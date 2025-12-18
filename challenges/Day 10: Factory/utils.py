from collections import deque

def bfs(current, memo, machine):
    # Using bfs to find minimum button presses
    queue = deque([(current, 0)])
    visited = set([machine.key(current)])

    while queue:
        state, steps = queue.popleft()
        if not any(state): return steps

        for button in machine.buttons:
            next_state = machine.apply(state, button)
            next_key = machine.key(next_state)
            if next_key not in visited: visited.add(next_key); queue.append((next_state, steps + 1))

    return float('inf')

class Machine(object):
    def __init__(self, goal, buttons, costs):
        self.goal = goal; self.buttons = buttons; self.costs = costs

    def key(self, state): return ''.join(list(map(lambda x: '#' if x else '.', state)))

    def apply(self, state, button):
        result = state.copy()
        for pos in button: result[pos] = not result[pos]
        return result
    
    def fewest_required_buttons(self):
        return bfs(self.goal, {}, self)