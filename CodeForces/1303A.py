t = int(input())
for _ in range(t):
    s = input().strip()
    first = s.find('1')
    last = s.rfind('1')
    if first == -1:
        print(0)
    else:
        count = s[first:last+1].count('0')
        print(count)
