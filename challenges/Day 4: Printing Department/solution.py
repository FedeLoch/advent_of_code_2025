input_path = 'challenges/Day 4: Printing Department/input'
from utils import dict_from_file, DIRS
from functools import reduce

DIRS_VALUES = DIRS.values()
grid = dict_from_file(input_path)

def is_accessible(grid, row, col):
    adjoining_rolls = 0
    for dr, dc in DIRS_VALUES:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '@':
           adjoining_rolls += 1

    return adjoining_rolls < 4

def accesible_rolls(grid):
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@' and is_accessible(grid, row, col): result += 1

    return result

def remove_once(grid):
    _grid, removable = grid.copy(), 0
    for row in range(len(_grid)):
        for col in range(len(_grid[0])):
            if grid[row][col] == '@' and is_accessible(grid, row, col):
                _grid[row][col] = '.'
                removable += 1

    return _grid, removable

def total_removable_rolls(grid):
    _grid, n = remove_once(grid)
    removable = n
    while (n != 0):
        _grid, n = remove_once(_grid)
        removable += n

    return removable

print('Part 1:', accesible_rolls(grid))
print('Part 2:', total_removable_rolls(grid))