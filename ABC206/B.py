n = int(input())
money = 0
day = 0
while True:
    day += 1
    money += day
    if money >= n:
        break
print(day)
