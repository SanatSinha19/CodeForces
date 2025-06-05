x = input().strip()
result = ''
 
for i, digit in enumerate(x):
    d = int(digit)
    if i == 0 and d == 9:
        result += '9'
    else:
        result += str(min(d, 9 - d))
 
print(result)