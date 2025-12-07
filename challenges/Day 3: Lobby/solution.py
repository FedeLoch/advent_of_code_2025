input_path = 'challenges/Day 3: Lobby/input'

part_1, part_2 = 0, 0

def max_pair(s):
    best = 0
    for i in range(len(s) - 1):
        right = max(s[i+1:])
        best = max(best, int(s[i] + right))
    return best

def max_n_digits(bank, n):
    stack, initial = [], len(bank) - n

    for battery in bank:
        while initial > 0 and stack and stack[-1] < battery:
          stack.pop(); initial -= 1
        stack.append(battery)

    return int("".join(stack[:n]))

with open(input_path) as f:
  for line in f:
    part_1 += max_pair(line[:-1])
    part_2 += max_n_digits(line[:-1], 12)

print('Part 1:', part_1)
print('Part 2:', part_2)