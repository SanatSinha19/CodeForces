n = int(input())
for i in range(n + 1):
    line = '  ' * (n - i)
    inc = list(range(i + 1))
    dec = list(range(i - 1, -1, -1))
    nums = inc + dec
    line += ' '.join(str(num) for num in nums)
    print(line)
for i in range(n - 1, -1, -1):
    line = '  ' * (n - i)
    inc = list(range(i + 1))
    dec = list(range(i - 1, -1, -1))
    nums = inc + dec
    line += ' '.join(str(num) for num in nums)
    print(line)
