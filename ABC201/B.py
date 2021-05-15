n = int(input())
pair = {}
for _ in range(n):
    s, t = map(str, input().split())
    pair[s] = int(t)

numbers = sorted(pair.values())
answer_value = numbers[-2]
for key, value in pair.items():
    if value == answer_value:
        print(key)
        exit(0)
