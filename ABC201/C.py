import itertools

s = input()
included = []
unknown = []
excluded = []
answer = []
for idx, char in enumerate(s):
    if char == 'o':
        included.append(str(idx))
    elif char == '?':
        unknown.append(str(idx))
    elif char == 'x':
        excluded.append(str(idx))

if len(included) > 4 or len(excluded) > 8:
    print(0)
    exit(0)
else:
    all_patterns = list(itertools.product(included+unknown, repeat=4))
    for part in all_patterns:
        is_valid = True
        for include_num in included:
            if include_num not in part:
                is_valid = False
                break
        if is_valid:
            answer.append(part)

print(len(answer))
