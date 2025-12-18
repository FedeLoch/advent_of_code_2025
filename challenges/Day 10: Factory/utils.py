from functools import reduce

def dp(current, memo, machine):
    if not any(current): return 0
    key = machine.key(current)

    if key not in memo:
        _min = float('inf')
        memo[key] = _min
        for button in machine.buttons:
            _min = min(_min, dp(machine.apply(current, button), memo, machine))
        memo[key] = _min + 1

    return memo[key]

class Machine(object):
    def __init__(self, goal, buttons, costs):
        self.goal = goal; self.buttons = buttons; self.costs = costs

    def key(self, state): return ''.join(list(map(lambda x: '#' if x else '.', state)))

    def apply(self, state, button):
        result = state.copy()
        for pos in button: result[pos] = not result[pos]
        return result
    
    def fewest_required_buttons(self):
        return dp(self.goal, {}, self)