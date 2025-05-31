from math import isqrt
t = int(input())
for _ in range(t):
    s = input().strip()
    num = int(s)
    sqrt_num = isqrt(num)
    if sqrt_num * sqrt_num != num:
        print("-1")
        continue
    found = False
    for a in range(sqrt_num + 1):
        b = sqrt_num - a
        if a >= 0 and b >= 0 and (a + b) * (a + b) == num:
            print(f"{a} {b}")
            found = True
            break
    if not found:
        print("-1")