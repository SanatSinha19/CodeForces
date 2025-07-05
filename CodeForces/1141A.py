n, m = map(int, input().split())

if m % n != 0:
    print(-1)
else:
    x = m // n
    count = 0
    for p in [2, 3]:
        while x % p == 0:
            x //= p
            count += 1
    if x == 1:
        print(count)
    else:
        print(-1)
