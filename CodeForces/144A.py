n = int(input())
a = list(map(int, input().split()))
max_height = max(a)
max_index = a.index(max_height)
min_height = min(a)
min_index = len(a) - 1 - a[::-1].index(min_height)
time = max_index + (n - 1 - min_index)
if min_index < max_index:
    time -= 1
print(time)