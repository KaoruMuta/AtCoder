n, k = map(int, input().split())
friends = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in friends.keys():
        friends[a] = b
    else:
        friends[a] += b

friends = sorted(friends.items(), key=lambda x: x[0])

for number, money in friends:
    if k - number >= 0:
        k += money

print(k)
