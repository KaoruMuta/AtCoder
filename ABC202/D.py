from math import factorial

a, b, k = map(int, input().split())
s = a + b
accumulated_count = 0
total_pattern_count = factorial(a+b) // (factorial(a)*factorial(b))
answer = ''

for i in range(s):
    current_count = factorial(s-i-1) // (factorial(max(a-1, 0))*factorial(b))
    if a > 0 and k <= accumulated_count + current_count:
        answer += 'a'
        a -= 1
    elif b > 0:
        answer += 'b'
        accumulated_count += current_count
        b -= 1
    elif a > 0:
        answer += 'a'
        a -= 1

print(answer)