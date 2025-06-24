n = int(input())
height = 0
used_cubes = 0
level = 1

while True:
    cubes_needed = level * (level + 1) // 2
    if used_cubes + cubes_needed > n:
        break
    used_cubes += cubes_needed
    height += 1
    level += 1

print(height)
