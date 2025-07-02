t = int(input())
for _ in range(t):
    n = int(input())
    print(2)
    last = n
    for i in range(n-1, 0, -1):
        print(last, i)
        last = (last + i + 1) // 2
