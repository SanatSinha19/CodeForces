x1, x2, x3 = map(int, input().split())
positions = sorted([x1, x2, x3])
meeting_point = positions[1]
total_distance = abs(x1 - meeting_point) + abs(x2 - meeting_point) + abs(x3 - meeting_point)
print(total_distance)
