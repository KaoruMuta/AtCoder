n = int(input())
a = list(map(int, input().split()))
answer = 0

for num in a:
    if num > 10:
        answer += num - 10

print(answer)
