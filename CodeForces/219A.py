k = int(input())
s = input()
from collections import Counter
cnt = Counter(s)
t = ""
for char in cnt:
    if cnt[char] % k != 0:
        print(-1)
        exit()
for char in cnt:
    t += char * (cnt[char] // k)
print(t * k)
