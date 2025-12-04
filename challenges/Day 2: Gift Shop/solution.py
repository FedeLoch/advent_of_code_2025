input_path = 'challenges/Day 2: Gift Shop/input'

found_invalid_ids, ranges, invalid_sum, max_len = set(), [], 0, 0

for _range in open(input_path).readlines()[0][:-1].split(','):
    low, high = map(int, _range.split('-'))
    ranges.append((low, high))
    max_len = max(max_len, len(str(high)))

for base_len in range(1, (max_len // 2) + 1):

    start = 10**(base_len - 1)
    if base_len == 1: start = 1
    
    for d in range(start, (10**base_len - 1) + 1):
        # generated invalid
        for k in range(2, max_len + 1):
            is_in_range = False
            total_len = base_len * k
            if total_len > max_len: break
                
            i = int(str(d) * k)
            
            if i in found_invalid_ids: continue
            
            for low, high in ranges:
                if low <= i <= high: is_in_range = True; break
            
            # found
            if is_in_range: found_invalid_ids.add(i); invalid_sum += i

print('Part 2:', invalid_sum)
