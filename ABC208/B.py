p = int(input())
money = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]

count = 0
while True:
    for m in money:
        if p >= m:
            p -= m
            count += 1
            break

    if p == 0:
        break

print(count)
