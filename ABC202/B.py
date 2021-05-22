s = input()
s = s[::-1]

answer = ''
for char in s:
    if char == '6':
        answer += '9'
    elif char == '9':
        answer += '6'
    else:
        answer += char

print(answer)
