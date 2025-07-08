n = int(input())
total = 0
for i in range(n):
    total += (i + 1) * (n - i) - i
print(total)
