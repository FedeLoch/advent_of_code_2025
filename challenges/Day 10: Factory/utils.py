from functools import reduce

def dp(current, memo, machine):
    print('current: ', current)
    if all(current): return 0
    key = ''.join(list(map(lambda x: '#' if x else '.', current)))

    if key not in memo:
        _min = float('inf')
        for button in machine.buttons:
            _min = min(_min, dp(machine.apply(current, button), memo, machine))
        memo[key] = _min + 1

    return memo[key]

class Machine(object):
    def __init__(self, goal, buttons, costs):
        self.goal = goal; self.buttons = buttons; self.costs = costs

    def apply(self, state, button):
        result = state.copy()
        for pos in button:
            result[pos] = not result[pos]
        return result
    
    def fewest_required_buttons(self):
        return dp(self.goal, {}, self)