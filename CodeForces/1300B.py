t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(abs(a[n] - a[n - 1]))
