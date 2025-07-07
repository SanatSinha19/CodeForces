t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a < c:
        ans1 = 1
    else:
        ans1 = -1
    if c < a * b:
        ans2 = b
    else:
        ans2 = -1

    print(ans1, ans2)
