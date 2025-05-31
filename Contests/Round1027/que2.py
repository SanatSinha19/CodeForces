def solve():
    n, k = map(int, input().split())
    s = input()
    c1 = s.count('1')
    c0 = n - c1
    if k > n // 2:
        print("NO")
        return
    c = n // 2 - k
    if c1 < c or c0 < c:
        print("NO")
        return
    lower = max(0, c1 - n // 2)
    upper = c1 + n // 2
    if k < lower or k > upper:
        print("NO")
        return
    if (c1 + k - n // 2) % 2 != 0:
        print("NO")
        return
    
    print("YES")
 
t = int(input())
for _ in range(t):
    solve()
