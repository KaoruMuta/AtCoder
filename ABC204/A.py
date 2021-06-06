x, y = map(int, input().split())
way = [0, 1, 2]
if x == y:
    print(x)
else:
    tmp = []
    tmp.append(x)
    tmp.append(y)
    for w in tmp:
        way.remove(w)
    print(way[0])
